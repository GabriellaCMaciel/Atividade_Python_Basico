print("\n------------------------")
print("       CABEÇALHO        ")
print("------------------------")

#Criando um dicionário
aluno = {
    "nome": "Gabriella Cunha Maciel", "disciplina": "Python Básico", "nota": "10"

}
#Usando as F-strings e acessando as chaves do dicionário
#
print(f" 👩🏻‍💻 Aluna: {aluno['nome']}")
print(f" 📚 Disciplina: {aluno['disciplina']}")
print(f" ✅ Nota: {aluno['nota']}")


from datetime import datetime
data_formada = datetime.now().strftime("%d/%m/%Y")

#Usando f-string para juntar o texto com a variável
print(f" 📅 Data {data_formada}")
#Saída: Data 16/06/2026
print("-------------------------------")