"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes


Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
"""

# Realizando o Import

from collections import Counter

# Exemplo 1

# Aqui podemos utilizar qualquer iterável
lista = [1, 1, 1, 2, 2, 3, 3, 8, 8, 8, 1, 99, 99]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)


# Exemplo 2
print(Counter('Geek University'))


# Exemplo 3
texto = """
Em 22 de julho de 1951, o Palmeiras realizou um dos maiores feitos de sua gloriosa trajetória. Foi neste dia, diante da
forte e estrelada Juventus-ITA, que o Verdão conquistou o Torneio Internacional de Clubes Campeões, consolidado no 
futebol como o primeiro campeonato mundial interclubes da história. O grito de campeão veio com uma vitória e um empate
diante da Vecchia Signora nas finais, disputadas no Maracanã lotado de brasileiros preenchidos de esperança e alegria 
no primeiro grande triunfo do Brasil no “período pós-Maracanazo”.
"""

palavras = texto.split()

res = (Counter(palavras))
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto

print(res.most_common(5))
