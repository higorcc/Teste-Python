"""
Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças:

1- As tuplas são representadas por parênteses ()

2- As tuplas são imutaveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação
em uma tupla gera uma nova tupla

"""

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado: tuplas com 1 elemento
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parentêses
# (4) Não é tupla
# (4,) É tupla
# 4, É tupla

# Podemos gerar uma tupla dinamicamente com o range
tupla = tuple(range(0, 11))
print(tupla)

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis
# Soma, valor máximo, valor minimo e tamanho são iguais as listas

# Tuplas não são mutáveis mas podemos sobrescrever seus valores. Exemplo:

tupla1 = tupla1 + tupla2
print(tupla1)

# Iterando sobre uma tupla
tupla = (1, 2, 3)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
print(tupla1.count(1))

# Verificando em qual indice um elemento está na tupla
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')

print(meses.index('Janeiro'))

# Exemplo 2
num_aleatorios = (1, 5, 6, 8, 7, 5, 5, 6, 6, 12, 1, 2, 3, 4)
print(num_aleatorios.index(5, 3))  # Nesta busca pelo index o primeiro valor dentro do parênteses é o
# valor a ser buscado e o segundo quer dizer a partir de qual indice

# Por quê utilizar tuplas

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro > Isso pq trabalhar com dados imutáveis traz mais segurança para o código
# - 
