print("\n------------------------")
print("       CABEÇALHO        ")
print("------------------------")

#Criando um dicionário
aluno = {
    "nome": "Gabriella Cunha Maciel", "disciplina": "Python Básico", "nota": "10"

}
#Usando as F-strings e acessando as chaves do dicionário
print(f" 👩🏻‍💻 Aluna): {aluno['nome']}")
print(f" 📚 Disciplina: {aluno['disciplina']}")
print(f" ✅ Nota: {aluno['nota']}")


from datetime import datetime
data_formada = datetime.now().strftime("%d/%m/%Y")

#Usando f-string para juntar o texto com a variável
print(f" 📅 Data {data_formada}")
#Saída: Data 16/06/2026
print("-------------------------------")

# ----- DESAFIO DA TABUADA (AULA 06) -----

print(" ----- TABUADA INTELIGENTE: MULTIPLICAÇÃO ----- ")

# Captura o número digitado pelo usuário
numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("--------------")

# O range(1, 11)vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for multiplicador in range (1, 11):
    resultado = numero * multiplicador
    print(numero, "x",multiplicador, "=", resultado)

    print("--------------")

print(" ----- TABUADA INTELIGENTE: ADIÇÃO ----- ")


numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("--------------")

# O range(1, 11)vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for multiplicador in range (1, 11):
    resultado = numero + multiplicador
    print(numero, "+",multiplicador, "=", resultado)

    print("--------------")


print(" ----- TABUADA INTELIGENTE: SUBTRAÇÃO ----- ")

numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("--------------")

# O range(1, 11)vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for multiplicador in range (1, 11):
    resultado = numero - multiplicador
    print(numero, "-",multiplicador, "=", resultado)

    print("--------------")


print(" ----- TABUADA INTELIGENTE: DIVISÃO ----- ")

numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero} = {resultado:.2f}")
print("--------------")

# O range(1, 11)vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for multiplicador in range (1, 11):
    resultado = numero / multiplicador
    print(f"{numero} / {multiplicador} = {resultado:.2f}")

    print("--------------")
