estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total = sum(estados.values())
for k, v in estados.items():
    porcent_estados = (v * 100)/total
    print(f"{k} representa {porcent_estados:.2f}% do total")