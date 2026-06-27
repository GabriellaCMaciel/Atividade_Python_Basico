import random
print("=" * 15)
print(" GABI FASHION STORE ")
print("=" * 15)

#--------------------
#FUNÇÃO 1 -Exibe mensagem de boas-vindas
#--------------------

def exibir_mensagem():
    print("\nBem-vindo(a)á nossa loja!")
    print("Hoje você poderá ganhar um cupom de descontos")

#FUNÇÃO 2 - Calcula desconto

def calcular_desconto(preco, percentual):
    desconto = preco * (percentual/100)
    preco_final = preco - desconto
    return preco_final

# Recebendo informações do usuário
nome_produto = input("\nDigite o nome do produto: ")

valor_produto = float(
    input("Digite o valor do produto: R$")
)


#Sorteando um cumpom de desconto
desconto_sorteado = random.choice([5, 10, 15, 20])

print(f"\n🎉 Parabéns! Você ganhou {desconto_sorteado}% de desconto!")

#Chamando a função para calcular

valor_final = calcular_desconto(
    valor_produto,
    desconto_sorteado

)

#xibindo resultado
print("\n-----RESUMO DA COMPRA-----")
print(f"Produto: {nome_produto}")
print(f"Valor original:R${valor_produto:.2f}")
print(f"Dsconto:{desconto_sorteado}%")
print(f"Valor final: R${valor_final:.2f}")
print("------------------------")