#Subindo primeira linha para o git     || TESTE||
def adicionar_ao_carrinho(produto_id, quantidade):
  # Busca o produto pelo ID
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        # Adiciona ao carrinho
        carrinho.append({"produto": produto, "quantidade": quantidade})
        print(f"{quantidade}x {produto['nome']} adicionado(s) ao carrinho.")
    else:
        print("Produto não encontrado!")