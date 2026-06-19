#PROFESSOR: Rodrigo Medeiros Vilela
#ALUNA: Gabriella Cunha Maciel
#COMPONENTE: Python Básico
#DATA: 12/06/26
# AULA 04

alunos_cadastrados = [
    "MARIA ROSÁRIO DE FÁTIMA DUARTE FERREIRA",
    "GABRIEL CARNEIRO BARROS",
    "LUIZ AUGUSTO XAVIER DE OLIVEIRA",
    "SEVERINO ITAMAR DA SILVA",
    "AMANDA CARDOSO RIBEIRO",
    "GABRIEL ALVES SABIA",
    "JULIANA BARBOSA FERREIRA",
    "ALEXANDRO HEITOR DOS SANTOS FERREIRA",
    "PEDRO CALDAS DE FARIAS",
    "GABRIELLA CUNHA MACIEL",
    "JULIO CESAR SOUZA RODRIGUES DOS SANTOS",
    "MIGUEL GUILHERME ALVES RODRIGUES",
    "LARA LORRANY GUEDES DIAS",
    "ALONSO DOS SANTOS SILVA",
    "PAULO VICTOR HAHN SIQUEIRA",
    "JESSICA CRISTINA GOMES PIMENTA DE OLIVEIRA",
    "DANIELLE MONTEIRO BRITO",
    "CARLOS HENRIQUE FELIX DA SILVA",
    "GABRIEL ANDRÉ DA SILVEIRA SILVA",
    "MIGUEL VÍTOR MENDES DA SILVA",
    "GUILHERME FEITOSA RODRIGUES DA SILVA",
    "MARIA LUIZA OLIVEIRA DE SÁ",
    "FRANCIELE MARIA FERREIRA",
    "ÁLEF CALEB AZEVEDO BRITO",
    "JOÃO FELLYPE ROCHA SANTANA",
    "PEDRO HENRIQUE ALVES BARBOSA RIBEIRO LEANDRO",
    "GILVANIR DOS SANTOS E SOUSA",
    "GABRIEL EVANGELISTA SILVA",
]
print(" -------------------- ALUNOS MATRICULADOS -------------------- \n", alunos_cadastrados, end="\n\n")

alunos_frequentes = alunos_cadastrados.copy()
alunos_frequentes.remove("MARIA ROSÁRIO DE FÁTIMA DUARTE FERREIRA")
alunos_frequentes.remove("SEVERINO ITAMAR DA SILVA")
alunos_frequentes.remove("AMANDA CARDOSO RIBEIRO")
alunos_frequentes.remove("GABRIEL ALVES SABIA")
alunos_frequentes.remove("PEDRO CALDAS DE FARIAS")
alunos_frequentes.remove("PAULO VICTOR HAHN SIQUEIRA")
alunos_frequentes.remove("JESSICA CRISTINA GOMES PIMENTA DE OLIVEIRA")
alunos_frequentes.remove("DANIELLE MONTEIRO BRITO")
alunos_frequentes.remove("CARLOS HENRIQUE FELIX DA SILVA")
alunos_frequentes.remove("MIGUEL VÍTOR MENDES DA SILVA")
alunos_frequentes.remove("MARIA LUIZA OLIVEIRA DE SÁ")
alunos_frequentes.remove("ÁLEF CALEB AZEVEDO BRITO")
alunos_frequentes.remove("GABRIEL EVANGELISTA SILVA")
print(" -------------------- LISTA DE ALUNOS ATUALIZADA POR FREQUÊNCIA -------------------- ")
print(alunos_frequentes, end="\n\n")

nomes_reformulados = [nome.title() for nome in alunos_frequentes]
print(" -------------------- NOMES REFORMULADOS -------------------- ")
print(nomes_reformulados, end="\n\n")

nomes_reformulados.sort()
print(" -------------------- POSIÇÃO CORRETA DOS ALUNOS -------------------- ")
print(nomes_reformulados, end = "\n\n")

print(" -------------------- RESULTADO FINAL -------------------- ")
print("O total de alunos matriculados foi:", len(alunos_cadastrados), "e a quantidade de alunos frequentes são de:", len(nomes_reformulados))