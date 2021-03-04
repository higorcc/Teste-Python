"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Enumerate -> Coloca uma string em ordem começando pela posição 0
             Retorna dois valores o indice e a string
             Obs: Quando não precisamos de um valor podemos descarta-lo utilizando o _
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)


# Exemplo de for 1 (Iterando uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in numeros:
    print(numero)

for _, letra in enumerate(nome):
    print(_)


qtd = int(input('Quantas vezes esse loop vai rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: ' ))
    soma = soma + num
print(f'A soma é {soma}')


qtd2 = 3
qtd = int(input('Digite um número '))
for qtd in range(qtd, qtd2+1):
    print('Higor')
