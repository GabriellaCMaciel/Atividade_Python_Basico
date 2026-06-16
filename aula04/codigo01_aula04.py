#PROFESSOR: Rodrigo Medeiros Vilela
#ALUNA: Gabriella Cunha Maciel
#COMPONENTE: Python Básico
#DATA: 12/06/26
# AULA 04

# Criar uma lista de strings chamada FRUTAS com 5 elementos
frutas=["manga", "abacate", "mexirica", "limão", "uva"]
print(frutas)

# Conta a quantidade de elementos na lista "frutas" e guarda a variável: "total_frutas"
total_frutas=len(frutas)

# Exibe na tela o valor da variável "total_frutas" (que é 5)
print("O total de frutas é: ", total_frutas, end="\n\n")

# Lista de alunos:
print("----------LISTA DE ALUNOS----------")

# Cria uma nova lista chamada "Alunos" com 5 nomes
alunos=["Juliana", "Lara", "Gabriel", "Alonso", "Gilvanir"]

# Exibe o primeiro nome da lista de "Alunos"
print("A primeira aluna é: ", alunos[0])

# Exibe os nomes da lista de "Alunos" em ordem
print("A segunda aluna é: ", alunos[1])
print("O terceiro aluno é: ", alunos[2])
print("O quarto aluno é: ", alunos[3])
print("O quinto aluno é: ", alunos[4], end="\n\n")

print("----------QUEBRA COM /N----------")

# O \n força a quebra de linha entre os itens
# Quando eu quiser concatenar uma string com uma variável
# (ou qualquer outra expressão Python) eu uso f" no início, antes da string e dentro do (),
# colocando a expressão Python dentro de {}
print(f"O primeiro aluno é: {alunos[0]}\nO segundo aluno é: {alunos[1]}", end="\n\n")

print("----------ADICIONAR ALUNO----------")

# Inserção: Adicionar o nome "Miguel" no final da lista
alunos.append("Miguel")
print(alunos, end="\n\n")

print("----------ADICIONAR EM POSIÇÃO ESPECÍFICA----------")

# Inserção 2: um aluno numa posição específica
alunos.insert(3,"Guilherme")
print(alunos, end="\n\n")

print("----------SEM SUCRILHOS AQUI!!----------")

# Exclusão: Remove um aluno da lista procurando pelo nome
alunos.remove("Guilherme")
alunos.remove("Miguel")
print(alunos, end="\n\n")

print("----------ESTÃO PERDOADOS...----------")
alunos.append("Miguel")
alunos.append("Guilherme")
print(alunos, end="\n\n")

print("----------TRAIRÁ AQUI NÃO :)----------")
alunos.remove("Guilherme")
print(alunos, end="\n\n")