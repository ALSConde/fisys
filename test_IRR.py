import numpy as np
from datetime import datetime
import numpy_financial as npf

# Dados de compra (fluxo de caixa negativo)
compras = [
    {"data": "03/01/2023", "valor": -171.48},
    {"data": "27/01/2023", "valor": -161.81},
    {"data": "27/01/2023", "valor": -91.71},
    {"data": "27/01/2023", "valor": -91.73},
    {"data": "17/04/2024", "valor": -38.32},
    {"data": "17/04/2024", "valor": -27.55},
    {"data": "15/05/2024", "valor": -39.62},
    {"data": "15/05/2024", "valor": -85.82},
    {"data": "18/11/2024", "valor": -456.99},
    {"data": "18/11/2024", "valor": -193.73},
]

# Dados de dividendos (fluxo de caixa positivo)
dividendos = [
    {"data": "13/02/2023", "valor": 2.08},
    {"data": "14/02/2023", "valor": 2.58},
    {"data": "13/03/2023", "valor": 1.74},
    {"data": "14/03/2023", "valor": 2.58},
    {"data": "14/04/2023", "valor": 2.10},
    {"data": "17/04/2023", "valor": 2.58},
    {"data": "12/05/2023", "valor": 1.90},
    {"data": "15/05/2023", "valor": 2.58},
    {"data": "14/06/2023", "valor": 2.10},
    {"data": "15/06/2023", "valor": 2.60},
    {"data": "13/07/2023", "valor": 1.60},
    {"data": "14/07/2023", "valor": 3.08},
    {"data": "11/08/2023", "valor": 1.40},
    {"data": "14/08/2023", "valor": 2.66},
    {"data": "31/08/2023", "valor": 1.56},
    {"data": "14/09/2023", "valor": 1.60},
    {"data": "15/09/2023", "valor": 1.10},
    {"data": "13/10/2023", "valor": 1.50},
    {"data": "16/10/2023", "valor": 2.66},
    {"data": "14/11/2023", "valor": 1.60},
    {"data": "16/11/2023", "valor": 2.66},
    {"data": "13/12/2023", "valor": 1.40},
    {"data": "14/12/2023", "valor": 2.66},
    {"data": "12/01/2024", "valor": 1.40},
    {"data": "15/01/2024", "valor": 2.66},
    
]

vendas = [
    {"data": "2025-01-07", "valor": 879.00},   # KNSC11
    {"data": "2025-01-07", "valor": 151.11},   # HGLG11
    {"data": "2025-01-07", "valor": 185.00},   # XPLG11
    {"data": "2025-01-07", "valor": 106.88},   # WEGE3
    {"data": "2025-01-07", "valor": 95.40},    # KLBN3
]


# Função para calcular a TIR
def calcular_tir(fluxos_de_caixa):
    datas = sorted(set(f["data"] for f in fluxos_de_caixa))
    fluxos_agrupados = {data: 0 for data in datas}
    for fluxo in fluxos_de_caixa:
        fluxos_agrupados[fluxo["data"]] += fluxo["valor"]

    datas_ordenadas = sorted(fluxos_agrupados.keys())
    valores = [fluxos_agrupados[data] for data in datas_ordenadas]

    tir = npf.irr(valores)
    return tir, datas_ordenadas, valores


# Combinar os fluxos de compras e dividendos
fluxos = compras + dividendos

# Adicionando os fluxos das vendas ao fluxo de caixa total
fluxos_de_caixa_final = fluxos + vendas

# Recalculando a TIR com o fluxo de caixa atualizado
tir, datas, valores = calcular_tir(fluxos_de_caixa_final)

tir_percent = tir * 100

# Imprimir a TIR
print(f"TIR: {tir_percent:.2f}%")
