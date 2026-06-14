#PROFESSOR: Rodrigo Medeiros Vilela
#ALUNA: Gabriella Cunha Maciel
#COMPONENTE: Python Básico
#DATA: 11/06/26
#AULA 03

# --- LIVE CODE: Aula 03 - Tipos de Dados e String ---

# 1. Trabalhando com números (int e float)
idade=int(input("Digite sua idade: "))
altura=float(input("Digite sua altura (ex: 1.75): "))

# 2. Manipulação de texto (Strings)
frase=input("Digite uma frase que você gosta: ")
print("\n----- ANALISANDO SEUS DADOS -----")

# 3. Fazendo cálculos simples com os números
print("Sua idade daqui a 5 anos será: ", idade + 5)
print("Sua altura em centímetros é: ", altura * 100, "cm")

# 4. Usando Métodos de Strings
# Explicando o que .upper(), .lower() e o len() fazem:
print("Sua frase toda em MAIÚSCULAS: ", frase.upper())
print("Sua frase toda em minúsculas: ", frase.lower())
print("A frase digitada tem", len(frase), "caracteres (incluindo espaços).")

