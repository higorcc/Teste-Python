"""
Listas em Python funcionam como vetores/matrizes em outras linguagens, com a diferença de serem dinâmico
e também de podermos colocar qualquer tipo de dado.

- Dinâmico: não possuem tamanho fixo
- Qualquer tipo de dado: Não possui tipo de dado fixo

As litas em Python são representadas por colchetes
"""

lista1 = [1, 4, 33, 2, 99, 8, 11, 13, 16, 25, 1, 26, 456]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = 'Geek University'

# Checar se existe determinado valor dentro da lista
numero = 7
if numero in lista4:
    print(f'Encontrei o {numero} \n')
else:
    print(f'Não encontrei o {numero} \n')

# Ordenar uma lista
lista1.sort()
print(lista1)


# Contar número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas :
"""
 Para adicionar elementos em listas, utilizamos a função append
"""
print(lista1)
lista1.append(5)
print(lista1)

# OBS: com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(4, 5, 89)  #Erro

lista1.append([6, 25, 34])  # Coloca a lista como elemento único (sublista)
print(lista1)

lista1.extend([1, 50, 44])  # Coloca cada elemento da lista como valor adicional
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS:isso nao substitui o valor inicial. O mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Inverter a lista
lista1.reverse()
print(lista1)

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos tem dentro da lista
print(len(lista6))

# Podemos remover o ultimo elemento de uma lista
print(lista1)
lista1.pop()
print(lista1)

# Podemos remover um elemento pelo indice
# Os elementos da direita serão deslocados para a esquerda
lista1.pop(3)
print(lista1)

# Podemos remover todos os itens da lista (zerar a lista)
lista6.clear()

# Convertendo uma string em uma lista
# Exemplo 1
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', ':Essencial']
print(lista6)

# O codigo abaixo significa: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Iterando sobre um produto
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ou digite 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(carrinho)

# Gerando indice em uma lista
cores = ['verde', 'amarelo', 'azul', 'vermelho']

for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(9))


# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)


# Soma, Valor máximo, Valor minimo, Tamanho
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


# Desempacotamento de listas

n1, n2, n3, n4, n5, n6 = lista

print(n1, n2, n3, n4, n5, n6)
