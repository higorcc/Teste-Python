""""
Mapas -> Conhecido em Python como dicionário

Dicionários em Python são conhecidos como chaves
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Iterando sobre um dicionário

for chave in receita:
    print(chave)

for valor in receita:
    print(receita[valor])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[valor]}')


