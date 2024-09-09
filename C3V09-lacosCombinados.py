#VERSÃO 01
#LAÇO ENQUANTO: EM SITUAÇÕES ONDE PODE DAR NENHUMA VOLTA OU DIVERSAS VOLTAS
#
#aprov = 0
#reprov = 0
#
#voltas = 1
#
#while voltas <= 10:
#    media = float(input("Digite a média: "))
#    if media >= 6:
#        aprov = aprov + 1
#    else:
#        reprov = reprov + 1
#    voltas = voltas + 1
#
#print(f"\nAprovados: {aprov}\nReprovados: {reprov}")
#------------------------------------------------------
#VERSÃO 02
#LAÇO REPITA: CONDICIONAL ONDE AO MENOS UMA VOLTA TEM QUER SER EXECUTADA E NO MAXIMO DIVERSAS
#
#aprov = 0
#reprov = 0
#
#voltas = 1
#
#while True:
#    media = float(input("Digite a média: "))
#    if media >= 6:
#        aprov = aprov + 1
#    else:
#        reprov = reprov + 1
#    voltas = voltas + 1
#    if voltas > 10:
#        break
#
#print(f"\nAprovados: {aprov}\nReprovados: {reprov}")
#------------------------------------------------------
#VERSÃO 03
#LAÇO FOR (PARA): SITUAÇÕES ONDE SABEMOS OS LIMITES (INICIO, FIM E INCREMENTO)

aprov = 0
reprov = 0
aluno = 1

for voltas in range(1,11,1):
    media = float(input(f"Digite a média do Aluno {aluno}: "))
    aluno = aluno + 1
    if media >= 6:
        aprov = aprov + 1
    else:
        reprov = reprov + 1

print(f"\nQuantidade de Aprovados: {aprov}\nQuantidade de Reprovados: {reprov}")