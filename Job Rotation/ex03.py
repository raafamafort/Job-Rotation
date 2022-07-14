faturamento_mes = []
for c in range(1, 5):
    faturamento_diario = float(input(f"Faturamento do dia {c}: "))
    if faturamento_diario != 0:
        faturamento_mes.append(faturamento_diario)
print(f"O menor valor de faturamento ocorrido em um dia do mês: {min(faturamento_mes)}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {max(faturamento_mes)}")
media = sum(faturamento_mes)/len(faturamento_mes)
for v in faturamento_mes:
    cont = 0
    if v > media:
        cont += 1
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {cont}")