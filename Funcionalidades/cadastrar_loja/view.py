# cadastrar_loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .form import StoreForm, ProductForm
from .models import Store, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def criar_loja(request):
    # se o usuário já tem loja, redireciona para editar
    try:
        store = request.user.store
    except Store.DoesNotExist:
        store = None

    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            messages.success(request, "Loja salva com sucesso.")
            return redirect('detalhe_loja')
    else:
        form = StoreForm(instance=store)
    return render(request, 'lojas/criar_loja.html', {'form': form})

@login_required
def detalhe_loja(request):
    store = getattr(request.user, 'store', None)
    return render(request, 'lojas/detalhe_loja.html', {'store': store})

@login_required
def criar_produto(request):
    store = getattr(request.user, 'store', None)
    if not store:
        messages.error(request, "Você precisa criar a loja primeiro.")
        return redirect('criar_loja')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            messages.success(request, "Produto cadastrado com sucesso.")
            return redirect('listar_produtos')
    else:
        form = ProductForm()
    return render(request, 'lojas/criar_produto.html', {'form': form})

@login_required
def listar_produtos(request):
    store = getattr(request.user, 'store', None)
    products = Product.objects.filter(store=store) if store else []
    return render(request, 'lojas/listar_produtos.html', {'products': products})
