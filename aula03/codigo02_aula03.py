#PROFESSOR: Rodrigo Medeiros Vilela
#ALUNA: Gabriella Cunha Maciel
#COMPONENTE: Python Básico
#DATA: 11/06/26
#AULA 03

# --- DESAFIO PRÁTICO ---

nome_completo=input("Digite o seu nome completo: ")
nome_limpo=nome_completo.replace("-", " ")
nome_padronizado=nome_limpo.upper()
print("Seu nome é:", nome_padronizado)
print("E tem", len(nome_padronizado), "caracteres")