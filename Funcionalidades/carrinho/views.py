from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
# Ajuste o caminho da importação do modelo Product
from Funcionalidades.cadastrar_loja.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'"{product.name}" foi adicionado novamente ao seu carrinho.')
    else:
        messages.success(request, f'"{product.name}" foi adicionado ao seu carrinho.')

    return redirect('home')

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_price = 0
    if cart:
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())

    return render(request, 'carrinho/detalhe_carrinho.html', {
        'cart': cart,
        'total_price': total_price,
    })


