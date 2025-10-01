from django.shortcuts import render, redirect
from Funcionalidades.carrinho.models import Cart

def finalizar_compra(request):
    # Garante que o usuário está logado
    if not request.user.is_authenticated:
        return redirect('index')  # ou outra página de login

    # Pega o carrinho do usuário, ou retorna vazio se não tiver
    cart, created = Cart.objects.get_or_create(user=request.user)
    produtos = cart.items.all()  # lista de CartItem
    total = sum(item.product.price * item.quantity for item in produtos)

    # Limpa o carrinho
    cart.items.all().delete()

    return render(request, 'comprar/resumo_compra.html', {
        'produtos': produtos,
        'total': total
    })
