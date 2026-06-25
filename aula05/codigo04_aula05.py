# Criando um verificador de preços inteligente
preco_alvo = 600.00
preco_atual = float(input("Digite o valor do produto $:"))
if preco_atual <= preco_alvo:
    print("Verificado: Preço acessível")
else:
    print("Negado: Está caro.")