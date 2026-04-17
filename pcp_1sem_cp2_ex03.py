
#Para os checkpoints
while True:
    nota_ck_1 = float(input("Qual sua nota do primeiro checkpoint? "))
    if 0 <= nota_ck_1 <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")

while True:
    nota_ck_2 = float(input("Qual sua nota do segundo checkpoint? "))
    if 0 <= nota_ck_2 <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")

while True:
    nota_ck_3 = float(input("Qual sua nota do terceiro checkpoint? "))
    if 0 <= nota_ck_3 <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")




#Para as Sprints
while True:
    sprint_1 = float(input("Qual sua nota do primeiro sprint? "))
    if 0 <= sprint_1 <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")

while True:
    sprint_2 = float(input("Qual sua nota do segundo sprint? "))
    if 0 <= sprint_2 <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")



#Para a GS
while True:
    gs = float(input("Qual sua nota da Global Solution? "))
    if 0 <= gs <= 10:
        break
    else:
        print("Insira uma nota válida! (De 0 a 10)")



#Ver a menor nota e calcular a media
def calcular_maior_checkpoints(nota1, nota2, nota3):
        if nota1 <= nota2 and nota1 <= nota3:
            menor = nota1
            maiores = (nota2, nota3)
        elif nota2 <= nota1 and nota2 <= nota3:
            menor = nota2
            maiores = (nota1, nota3)
        else:
            menor = nota3
            maiores = (nota1, nota2)

        soma = maiores[0] + maiores[1]
        media = soma / 2

        return media, maiores

resultado_media, notas_usadas = calcular_maior_checkpoints(nota_ck_1, nota_ck_2, nota_ck_3)

print(f"As duas maiores notas foram: {notas_usadas[0]} e {notas_usadas[1]}")



# CORRIJA ISSO

#
# #Media simples
# media_simples = float((notas_usadas[0] + notas_usadas[1]) + (sprint_1 + sprint_2)/4)
#
# peso1 = float(media_simples * 0.4)
# peso2 = float(gs * 0.6)
#
# media_do_semestre = float(peso1 + peso2)
#
# mediaPeso = media_do_semestre * 0.4
#
# #Exibir os resultados
# print(f"A media do semestre, sem os pesos é de: {media_do_semestre:.2f}")
# print(f"A media do semestre, com os pesos é de: {mediaPeso:.2f}")