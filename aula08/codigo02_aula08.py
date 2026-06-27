import random

# Definindo a função que faz o sorteio
def rolar_dado():
    numero = random.randint(1, 6)
    return numero

print(" --- JOGO DE DADOS --- ")

# Loop contínuo para o usuário jogar quantas vezes quiser
while True:
    acao = input("Digite 'rolar' para o dado rolar ou 'sair' para encerrar: ")

    if acao == "sair":
        print("Até a próxima!")
        break  # Quebra o loop

    elif acao == "rolar":
        resultado = rolar_dado()  # Chama a função
        print(f"🎲 Resultado: {resultado}\n")

    else:
        print("Comando inválido. Tente novamente.")