print("===SITEMA BANCÁRIO DE FINANCIAMENTO===")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
renda = float(input("Renda mensal: R$ "))
valor_financiado = float(input("Valor do emprestimo: R$ "))
parcelas = int(input("Quantidade de parcelas (3 a 24): "))

def pode_aprovar(idade, renda, valor):
    # Retorna true se tiver 18+ anos e o valor for <= 20xa renda
    return idade >= 18 and valor <= (renda * 20)

def definir_taxa(parcelas):
    if parcelas <=6:
        return 0.05 #5%
    elif parcelas <= 12:
        return 0.08 #8%
    else:
        return 0.10 #10%

def calcular_parcela(valor, taxa, parcelas):
    numerador = taxa * (1 + taxa)**parcelas
    denominador = (1 + taxa)**parcelas - 1
    return valor * (numerador / denominador)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

if pode_aprovar(idade, renda, valor_financiado):
    taxa = definir_taxa(parcelas)
    valor_parcela = calcular_total(valor_financiado, taxa, parcelas)
    valor_total = calcular_juros(valor_parcela, parcelas)
    valor_juros = calcular_juros(valor_total, valor_financiado)

print(f"\nok PARABENS, {nome}! Seu financiamento foi aprovado.")
print(f"Taxa aplicada: {taxa*100}% ao mes.")
print(f"Valor da Parcela: R${valor_parcela:.2f}")
print(f"Total de Juros: R${valor_juros:.2f}")

else:
print(f"\nnot DESCULPE, {nome}. Financiamento negado.")
print("Motivo: Idade menor que 18 anos ou valor solicitado acima de 20x da sua renda.")
