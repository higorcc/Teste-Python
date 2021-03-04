"""
Módulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.
"""

from collections import OrderedDict

# Entendendo a diferença entre um dict comum e OrderedDict

# Dicionario comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)   # É retornado "True" porque o dicionário comum não importa a ordem, apenas armazena


# OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)   # É retornado "False" porque a ordem importa para o OrderedDict
