"""
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()
print(ret)
---
OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.
"""


# Exemplo 1
def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())


# Refatorando a primeira função
def diz_oi():
    return 'Oi '


nome = input('Informe o nome: ')
print(diz_oi() + nome)

"""
OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""


# Exemplo 1
def diz_oi2():
    print('Estou sendo executado antes do return')
    return 'Salve!'
    print('Estou sendo executado depois do return')


print(diz_oi2())


# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 1
    elif variavel is None:
        return 0
    return 2


print(nova_funcao())


# Exemplo 3
from random import random
def joga_moeda():
    if random() < 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

