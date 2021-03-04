"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
charmar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo


Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""


# Exemplo
def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(2, 2))
print(soma_todos_numeros(5, 8, 3))


# Outro exemplo de utilização de args
def informacoes(nome, sobrenome, *args):
    print(f'{nome} {sobrenome} {args}')


informacoes('Higor', 'Campos')
informacoes('Higor', 'Campos', 23, 'higorccruz@gmail.com')


# Desempacotamento de listas(ou tuplas)
numeros = [4, 5, 8, 6]
print(soma_todos_numeros(*numeros))
