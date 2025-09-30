from django.shortcuts import render

def finalizar_compra(request):
    # Pega carrinho da sessão, ou cria vazio se não existir
    carrinho = request.session.get('carrinho', [])

    # Calcula total
    total = sum(produto['preco'] for produto in carrinho)

    # Faz cópia dos produtos para mostrar no template
    produtos = carrinho.copy()

    # Limpa o carrinho
    carrinho.clear()
    request.session['carrinho'] = carrinho

    # Renderiza o template existente
    return render(request, 'comprar/resumo_compra.html', {'produtos': produtos, 'total': total})

