import csv

tipo = input("Tipo (apartamento/casa/estudio): ").lower()
valor = 0

if tipo == "apartamento":
    valor = 700
    quartos = int(input("Quantos quartos? "))
    if quartos == 2:
        valor += 200

    garagem = input("Quer garagem? (s/n): ").lower()
    if garagem == "s":
        valor += 300

    filhos = input("Tem filhos? (s/n): ").lower()
    if filhos == "n":
        valor *= 0.95

elif tipo == "casa":
    valor = 900
    quartos = int(input("Quantos quartos? "))
    if quartos == 2:
        valor += 250

    garagem = input("Quer garagem? (s/n): ").lower()
    if garagem == "s":
        valor += 300

elif tipo == "estudio":
    valor = 1200
    vagas = int(input("Quantas vagas? "))
    if vagas >= 2:
        valor += 250 + (vagas - 2) * 60

print("\nValor do aluguel:", valor)

# contrato
contrato = 2000
parcelas = int(input("Parcelar contrato (até 5x): "))
print("Valor da parcela:", contrato / parcelas)

# gerar CSV
with open("pagamentos.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Mês", "Valor"])

    for mes in range(1, 13):
        writer.writerow([mes, valor])

print("Arquivo CSV gerado!")