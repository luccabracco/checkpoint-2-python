estado_origem = int(input("Digite o estado de origem da carga (1 a 5): "))
peso_carga = int(input("Digite o peso da carga em Tonaledas: "))
codigo_carga = int(input("Digite o codigo da carga (10 a 40): "))

if 10 <= codigo_carga <= 20:
    preco_por_kg = 100
elif 20 <= codigo_carga <= 30:
    preco_por_kg = 250
elif 30 <= codigo_carga <= 40:
    preco_por_kg = 340
else:
    preco_por_kg = 0
    print("Codigo de carga errado!")

if estado_origem == 1:
    porcentagem_imposto = 0.35
elif estado_origem == 2:
    porcentagem_imposto = 0.25
elif estado_origem == 3:
    porcentagem_imposto = 0.15
elif estado_origem == 4:
    porcentagem_imposto = 0.05
elif estado_origem == 5:
    porcentagem_imposto = 0.0
else:
    porcentagem_imposto = 0
    print("Estado de origem invalido")

peso_carga_quilos = peso_carga * 1000
preco_carga = peso_carga_quilos * preco_por_kg
valor_imposto = preco_carga * porcentagem_imposto
valor_total = preco_carga + valor_imposto

print(f"O peso da carga em quilos é {peso_carga_quilos}")
print(f"O preco da carga é de R${preco_carga:.2f}")
print(f"O valor do imposto cobrado é de R${valor_imposto:.2f}")
print(f"O valor total é de R${valor_total:.2f}")