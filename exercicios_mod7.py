"""
# 1
a = [1, 0, 5, -2, -5, 7]
## Somando a posição 0, 1 e 5 da lista
soma = (a[0] + a[1] + a[5])
print(soma)
## Modificar a lista na posição 4
for i in a:
    if i == a[4]:
        a[4] = 100
print(a)
## Mostrar todos os elementos da lista, um em cada linha
for i in a:
    print(i)

# 2
lista = []
indice = 0
while True:
    indice += 1
    valor = int(input(f'{indice}/6 - Informe um número inteiro: '))
    lista.append(valor)
    if len(lista) == 6:
        break
for i in lista:
    print(i, end=" ")

# 3
numeros = []
quadrado = []
indice = 0
while indice < 10:
    indice += 1
    n = int(input(f'{indice}/10 - Informe o valor para calcular o quadrado: '))
    numeros.append(n)
for i in numeros:
    res = i * i
    quadrado.append(res)
print(f'Números: {numeros}')
print(f'Ao quadrado: {quadrado}')

# 4
lista = []
indice = 0
while indice < 8:
    indice += 1
    n = int(input(f'{indice}/8 - Informe um número para adicionar ao vetor: '))
    lista.append(n)
print('-' * 30)
print(lista)
p1 = int(input('Informe a 1ª posição do vetor para somar: '))
p2 = int(input('Informe a 2ª posição do vetor para somar: '))
if p1 < 0 or p1 > len(lista) or p2 < 0 or p2 > len(lista):
    print('Posição inválida')
else:
    print(f'O resultado da soma é {lista[p1] + lista[p2]}')

# 5
lista = []
indice = 0
cont = 0
while indice < 10:
    indice += 1
    n = int(input(f'{indice}/10 -Informe um número pra adicionar ao vetor: '))
    lista.append(n)
for i in lista:
    if i % 2 == 0:
        cont += 1
print(f'A lista possui {cont} números pares')

# 6
lista = []
indice = 0
while indice < 10:
    indice += 1
    n = int(input(f'{indice}/10 -Informe um número pra adicionar ao vetor: '))
    lista.append(n)
print('-' * 15)
print(f'O maior número é: {max(lista)}')
print(f'O menor número é: {min(lista)}')


# 7
lista = []
indice = 0
cont = -1
while indice < 10:
    indice += 1
    n = int(input(f'{indice}/10 -Informe um número pra adicionar ao vetor: '))
    lista.append(n)
maior = max(lista)
for i in lista:
    cont += 1
    if i == maior:
        break
print(f'O maior número é {maior} e está na posição {cont}')

# 8
indice = 0
lista = []
while indice < 6:
    indice += 1
    n = int(input(f'{indice}/6 - Informe o número: '))
    lista.append(n)
lista.reverse()
print(f'Ordem inversa: {lista}')

# 9
indice = 0
lista = []
while indice < 6:
    indice += 1
    n = int(input(f'{indice}/6 Informe um número par: '))
    if n % 2 == 0:
        lista.append(n)
    else:
        print('O número não é par')
        indice -= 1
lista.reverse()
print(f'A ordem inversa dos números pares informados é: {lista}')

# 10
lista = []
indice = 0
while indice < 15:
    indice += 1
    nota = float(input(f'Informe a nota do {indice}º aluno: '))
    if nota < 0 or nota > 10:
        indice -= 1
        print('A nota deve ser maior que zero e menor que 10')
    else:
        lista.append(nota)
print(f'A média das notas é {sum(lista) / len(lista)}')

# 11
from random import randrange
lista = []
cont = 0
soma = 0
while True:
    n = randrange(-10, 10)
    lista.append(n)
    if n < 0:
        cont += 1
    else:
        soma += n

    if len(lista) == 10:
        break
print(f'A lista possui {cont} números negativos\n'
      f'A soma dos positivos é {soma}')
print(lista)

# 12
from random import randrange
lista = []
for i in range(1, 5 + 1):
    n = randrange(1, 10 + 1)
    lista.append(n)
print(lista)
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(f'Média: {sum(lista) / len(lista)}')

# 13
from random import randrange
lista = []
cont = -1
cont2 = -1
for i in range(1, 5 + 1):
    n = randrange(1, 50 + 1)
    lista.append(n)
print(f'Menor número: {min(lista)} - Posição: {lista.index(min(lista))}')
print(f'Maior número: {max(lista)} - Posição: {lista.index(max(lista))}')
print(lista)

# 14
from random import randrange
lista = []
aux = []
repetidos = []
for i in range(1, 10 + 1):
    lista.append(randrange(1, 10 + 1))
for i in lista:
    if i in aux:
        repetidos.append(i)
    else:
        aux.append(i)
print(repetidos)
print(lista)

# 15
from random import randrange
lista = []
aux = []
for i in range(1, 20 + 1):
    n = randrange(1, 20)
    lista.append(n)
print(lista)
#
for i in lista:
    if i not in aux:
        aux.append(i)
print(aux)


# 16
indice = 0
lista = []
while indice < 5:
    indice += 1
    n = float(input(f'{indice}/5 - Informe o número:'))
    lista.append(n)
while True:
    print('-' * 30)
    opcao = int(input('0 - Sair do programa\n'
                      '1 - Imprimir a lista na ordem direta\n'
                      '2 - Imprimir a lista na ordem inversa\n'
                      'Informe a opção: '))
    if opcao == 0:
        break
    elif opcao == 1:
        print(lista)
    elif opcao == 2:
        lista.reverse()
        print(lista)
    else:
        print('Código inválido')

# 17
from random import randrange
posicao = -1
# Criando a lista
lista = []
for i in range(1, 20 + 1):
    n = randrange(-10, 10 + 1)
    lista.append(n)
print(lista)
#
for i in lista:
    posicao += 1
    if i < 0:
        lista[posicao] = 0
print(lista)

# 18
from random import randrange
posicao = -1
# Criando a lista
lista = []
for i in range(1, 20 + 1):
    n = randrange(1, 20 + 1)
    lista.append(n)
print(lista)
#
num = int(input('Informe um número para saber os seus multiplos dentro da lista: '))
for i in lista:
    if num % i == 0:
        print(i, end=" ")

# 19
lista = []
posicao = -1
while len(lista) < 50:
    posicao += 1
    lista.append((posicao + 5 * posicao) % (posicao + 1))
print(lista)
print(len(lista))

# 20
lista = []
lista2 = []
indice = 0
while len(lista) < 10:
    indice += 1
    n = int(input(f'{indice}/10 Informe um número entre 1 e 50: '))
    if n < 1 or n > 50:
        print('O número está fora do solicitado')
        indice -= 1
    else:
        lista.append(n)
        if n % 2 != 0:
            lista2.append(n)
print(f'Lista: {lista}')
print(f'Lista somente com impares: {lista2}')

# 21
posicao = -1
lista = []
lista2 = []
lista_res = []
while len(lista) < 10:
    n1 = int(input('Informe o número:'))
    lista.append(n1)
print('Fim da primeira lista')
while len(lista2) < 10:
    n2 = int(input('Informe o número:'))
    lista2.append(n2)
print('Fim da segunda lista')
while len(lista_res) < 10:
    posicao += 1
    res = lista[posicao] - lista2[posicao]
    lista_res.append(res)
print(f'Lista 1 : {lista}')
print(f'Lista 2 : {lista2}')
print(f'Resultados : {lista_res}')

# 22
# Criação da lista
posicao1 = -2
posicao2 = -1
lista1 = []
lista2 = []
lista3 = []
while len(lista1) < 10:
    n1 = int(input('Informe o número:'))
    lista1.append(n1)
print('Fim da primeira lista')
#
while len(lista2) < 10:
    n2 = int(input('Informe o número:'))
    lista2.append(n2)
print('Fim da segunda lista')
while len(lista3) < 10:
    posicao1 += 2
    posicao2 += 2
    lista3.append(lista1[posicao1])
    lista3.append(lista2[posicao2])
print(f'Lista 1 : {lista1}')
print(f'Lista 2 : {lista2}')
print(f'Lista 3 : {lista3}')

# 23
posicao = -1
soma = 0
lista1 = []
lista2 = []
while len(lista1) < 5:
    n1 = int(input('Informe o número a inserir: '))
    lista1.append(n1)
print('Fim da primeira lista')
while len(lista2) < 5:
    n2 = int(input('Informe o número a inserir: '))
    lista2.append(n2)
while posicao < len(lista1) - 1:
    posicao += 1
    soma += (lista1[posicao] * lista2[posicao])
print(soma)

#23 (Solução melhor)
soma = 0
lista1 = []
lista2 = []
while len(lista1) < 5:
    n1 = int(input('Informe o número a inserir: '))
    lista1.append(n1)
print('Fim da primeira lista')
while len(lista2) < 5:
    n2 = int(input('Informe o número a inserir: '))
    lista2.append(n2)
for i in range(5):
    soma += (lista1[i] * lista2[i])
print(soma)

# 24
dicio = {}
for x in range(10):
    print("Digite o número do aluno: ")
    numeroaluno = int(input())
    print("Digite a altura do aluno: ")
    alturaaluno = float(input())
    dicio.update({numeroaluno: alturaaluno})
print(dicio)
mini = min(dicio.values())
maxi = max(dicio.values())
for chave, valor in dicio.items():
    if valor == mini:
        print(f"O aluno mais baixo da sala tem o número {chave} e mede {valor:.2f}.")
    elif valor == maxi:
        print(f"O aluno mais alto da sala tem o número {chave} e mede {valor:.2f}.")

# 25
lista = []
i = 0
while True:
    i += 1
    if i % 7 != 0 and list(str(i))[-1] != '7':
        lista.append(i)
    if len(lista) == 100:
        break
print(lista)

# 26

# 27
lista = []
while len(lista) < 10:
    n = int(input('Informe um número: '))
    lista.append(n)
for elemento in lista:
    cont = 0
    for numero in range(1, elemento + 1):
        res = elemento % numero
        if res == 0:
            cont += 1
    if cont == 2:
        print(f'Número: {elemento}, Posição: {lista.index(elemento)}')
print(lista)

# 28
from random import randrange
v = []
v1 = []
v2 = []
while len(v) < 10:
    n = randrange(1, 20 + 1)
    v.append(n)
for elemento in v:
    if elemento % 2 == 0:
        v1.append(elemento)
    else:
        v2.append(elemento)
print(v1)
print(v2)
print(v)

# 29
indice = 0
pares = []
impares = []
while indice < 6:
    indice += 1
    n = int(input(f'{indice}/6 - Digite 6 valores: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('Números pares: ')
for i in pares:
    print(i, end=" ")
print(f'Soma: {sum(pares)}')
print('-' * 30)
print('Números impares: ')
for j in impares:
    print(j, end=" ")
print(f'Quantidade: {len(impares)}')

# 30
v = []
v1 = []
v2 = []
# Criação das duas listas
while len(v1) < 10:
    n1 = int(input('Informe os números para o primeiro vetor: '))
    v1.append(n1)
print('Fim do primeiro vetor')
while len(v2) < 10:
    n2 = int(input('Informe os números para o segundo vetor: '))
    v2.append(n2)
print('Fim do segundo vetor')
#
for elemento in v1:
    for elemento2 in v2:
        if elemento == elemento2 and elemento not in v:
            v.append(elemento)
print(v)
print(v1)
print(v2)

# 31
v = []
v1 = []
v2 = []
# Criação das duas listas
while len(v1) < 10:
    n1 = int(input('Informe os números para o primeiro vetor: '))
    v1.append(n1)
print('Fim do primeiro vetor')
while len(v2) < 10:
    n2 = int(input('Informe os números para o segundo vetor: '))
    v2.append(n2)
print('Fim do segundo vetor')
#
for elemento in v1:
    if elemento not in v:
        v.append(elemento)
for elemento2 in v2:
    if elemento2 not in v:
        v.append(elemento2)
print(v)
print(v1)
print(v2)

# 32
# Criação das listas
v1 = []
v2 = []
resultados = []
while len(v1) < 5:
    n = int(input('Informe os números do primeiro vetor: '))
    if n in v1:
        print('Não é permitido valores repetidos')
    else:
        v1.append(n)
print('Fim do primeiro vetor')
while len(v2) < 5:
    n = int(input('Informe os números do segundo vetor: '))
    if n in v2:
        print('Não é permitido valores repetidos')
    else:
        v2.append(n)
print('Fim do segundo vetor')
# Soma dos valores na mesma posição
for i in range(0, 5):
    res = v1[i] + v2[i]
    resultados.append(res)
print(f'Soma: {resultados}')
resultados.clear()
# Multiplicação dos valores na mesma posição
for i in range(0, 5):
    res = v1[i] * v2[i]
    resultados.append(res)
print(f'Multiplicação: {resultados}')
resultados.clear()
# Números que existem em V1 mas não em V2
for i in v1:
    if i not in v2:
        resultados.append(i)
print(f'Números que estão somente no primeiro vetor: {resultados}')
resultados.clear()
# Interseção entre V1 e V2
for i in v1:
    if i in v2:
        resultados.append(i)
print(f'Números que estão nos dois vetores: {resultados}')
resultados.clear()
# União entre V1 e V2
resultados = v1.copy()
for i in v2:
    if i not in resultados:
        resultados.append(i)
print(f'Todos os elementos, sem repetição {resultados}')
print('')
print(v1)
print(v2)

# 33
lista = []
while len(lista) < 15:
    n = int(input('Informe o valor a ser adicionado a lista: '))
    lista.append(n)
print(lista)
for i in lista:
    if i == 0:
        lista.pop(lista.index(i))
print(lista)

# 34
lista = []
while len(lista) < 10:
    n = int(input('Informe 10 números diferentes: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Este número já foi informado.')
print(lista)

# 35
va = list(input('Digite o primeiro número: '))
vb = list(input('Digite o segundo número: '))
va.reverse()
vb.reverse()
soma = list()
count_aux = 0

for i in range(len(va), 5):
    va.append(0)
for i in range(len(vb), 5):
    vb.append(0)

for i in range(5):
    s = int(va[i]) + int(vb[i]) + count_aux
    if s >= 10:
        s -= 10
        soma.append(s)
        count_aux = 1
    else:
        soma.append(s)
        count_aux = 0

soma.reverse()
print(f'Soma: {soma}')


#Opcional para eliminar os zeros a esquerda do resultado da soma de A e B
i = 0
while soma[i] == 0:
    soma.pop(i)

print(f'Soma: {soma}')

# 36
lista = []
while len(lista) < 10:
    n = float(input('Informe 10 números para adicionar a lista: '))
    lista.append(n)
lista.sort()
print(lista)

# 37
lista = [1, 2, 345, 1, 0, 12, 0, 12, 5, 7, 0, 3, 0]
lista.sort()
a1 = (lista[0:5]).copy()
lista.sort(reverse=True)
a1.extend(lista[0:5])
print(a1)

"""



