"""
Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Forma geral

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo 1 em 1)

Gerar uma lista de números:
lista = list(range(0,10))
"""

# Forma 1 (declarando valor final)
for num in range(11):
    print(num)

# Forma 2 (declarando valor do inicio e do fim)
for num in range(1, 11):
    print(num)

# Forma 3 (declarando valor do inicio, fim e passo)
for num in range(1, 11, 3):
    print(num)


