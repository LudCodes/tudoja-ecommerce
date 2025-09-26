# funcionalidades/comprar.py

def finalizar_compra(carrinho):
    if not carrinho:
        print("Seu carrinho está vazio!")
        return

    print("\n--- Resumo da Compra ---")
    total = 0
    for produto in carrinho:
        print(f"- {produto['nome']} - R$ {produto['preco']:.2f}")
        total += produto['preco']

    print(f"\nTotal: R$ {total:.2f}")
    print("Compra finalizada com sucesso! Obrigado pela preferência.\n")

    # limpar o carrinho após a compra
    carrinho.clear()
