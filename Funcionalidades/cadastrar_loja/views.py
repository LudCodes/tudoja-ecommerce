# cadastrar_loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .form import StoreForm, ProductForm
from .models import Store, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ------------------------------
# VIEWS DO DONO DA LOJA (PAINEL)
# ------------------------------

@login_required
def criar_loja(request):
    # Tenta obter a loja do usuário, se existir
    store = getattr(request.user, 'store', None)

    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            messages.success(request, "Loja salva com sucesso.")
            return redirect('detalhe_loja')
        else:
            messages.error(request, "Erro ao salvar a loja. Verifique os dados.")
    else:
        form = StoreForm(instance=store)

    return render(request, 'lojas/criar_loja.html', {'form': form})


@login_required
def detalhe_loja(request):
    store = getattr(request.user, 'store', None)
    if not store:
        messages.info(request, "Você ainda não possui uma loja.")
        return redirect('criar_loja')
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
            messages.error(request, "Erro ao cadastrar produto. Verifique os dados.")
    else:
        form = ProductForm()

    return render(request, 'lojas/criar_produto.html', {'form': form})


@login_required
def listar_produtos(request):
    store = getattr(request.user, 'store', None)
    if not store:
        messages.info(request, "Você ainda não possui produtos cadastrados.")
        return redirect('criar_loja')

    products = Product.objects.filter(store=store)
    return render(request, 'lojas/listar_produtos.html', {'products': products})


# ------------------------------
# VIEWS PARA CLIENTES / VITRINE
# ------------------------------

def home(request):
    # Pega todos os produtos ativos
    products = Product.objects.filter(active=True)
    return render(request, 'lojas/home.html', {'products': products})

def loja_detalhe(request, store_id):
    """
    Página de produtos de uma loja específica
    """
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store)
    return render(request, 'lojas/loja_detalhe.html', {'store': store, 'products': products})
