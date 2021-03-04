"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Importando
from collections import namedtuple

# Precisamos definir nome e parâmetros

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ragnar = cachorro(idade=5, raca='Pitbull', nome='Ragnar')
toby = cachorro(idade=5, raca='Pitbull', nome='Toby')
maxx = cachorro(idade=5, raca='Pitbull', nome='max')


print(ragnar)

# Acessando os dados

# Forma 1
print(ragnar[0])   # Idade
print(ragnar[1])   # Raça
print(ragnar[2])   # Nome

# Forma 2
print(ragnar.idade)
print(ragnar.raca)
print(ragnar.nome)
