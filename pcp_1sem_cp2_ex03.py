print("------------- CALCULADORA DA MEDIA SEMESTRAL -------------")

#nota para os checkpoints
while True:
    c1 = float(input("Qual a sua primeira nota do checkpoint? "))
    if 0 <= c1 <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")

while True:
    c2 = float(input("Qual a sua segunda nota do checkpoint? "))
    if 0 <= c2 <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")

while True:
    c3 = float(input("Qual a sua terceira nota do checkpoint? "))
    if 0 <= c3 <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")

print()

#nota para as sprints
while True:
    sp_1 = float(input("Qual a sua primeira nota da sprint? "))
    if 0 <= sp_1 <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")

while True:
    sp_2 = float(input("Qual a sua segunda nota da sprint? "))
    if 0 <= sp_2 <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")

print()

#nota para a gs
while True:
    gs = float(input("Qual a sua primeira nota da global solution? "))
    if 0 <= gs <= 10:
        break
    else:
        print("Insira uma nota valida!(De 0 a 10)")


#descobrir a menor nota do checkpoint

def menor_nota(c1, c2, c3):
    if c1 <= c2 and c1 <= c3:
       return c1
    elif c2 <= c3:
        return c2
    else:
        return c3

nota_descartada = menor_nota(c1, c2, c3)
#print(nota_descartada)

print()

#Calcular a media
media = ((c1 + c2 + c3 - nota_descartada + sp_1 + sp_2) /4) * 0.4 + (gs * 0.6 )

#Media com peso
media_peso = media * 0.4


print(f"A media sem peso é {media:.1f}")
print(f"A media com peso é {media_peso:.1f}")