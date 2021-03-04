"""
Dicionarios

Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {}

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos "chave:valor"
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
"""

# Criação de dicionários
# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# print(paises['ar'])   Caso tentarmos fazer acesso utilizando chave não existente, teremos o KeyError


# Forma 2 - Acessando via get (Recomendada)
print(paises.get('br'))
print(paises.get('ar'))


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla,
# como chaves de dicionarios

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as
# mesmas são imutáveis

localidades = {
    (35.895, 39.887): 'Escritório em Tókio',
    (44.778, 49.856): 'Escritório em Nova York',
    (11.556, 15.698): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 200}

print(receita)

# Forma 1 - mais comum

receita['abr'] = 300
print(receita)

# Forma 2  - receita.update({'mai':320})

novo_dado = {'mai': 320}

receita.update(novo_dado)
print(receita)


# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 500
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO: A forma de adicionar novos elementos e atualizar em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, não podemos ter chaves repetidas

# Remover dados de um dicionário
# Forma 1 - Mais comum
# Aqui precisamos sempre informar a chave
receita.pop('mai')

# Forma 2
del receita['fev']


# Comercio eletronico, onde temos um carrinho de compras no qual adicionamos produtos
"""
Carrinho de compras
    Produto 1
        - nome;
        - quantidade;
        - valor;
    Produto 2
        - nome;
        - quantidade;
        - valor;
"""

# Poderíamos utilizar uma lista

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['Fifa 21', 1, 250.00]

carrinho = []

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Utilizando Tuplas

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Fifa 21', 1, 250.00)

carrinho = (produto1,produto2)

print(carrinho)

# Utilizando Dicionário

produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'Fifa 21', 'quantidade': 1, 'preço': 250.00}

carrinho = []

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

