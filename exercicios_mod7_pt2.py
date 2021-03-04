"""
# 1
matriz = [[8, 4, 5, 12], [14, 33, 12, 1], [16, 8, 3, 1], [9, 99, 3, 32]]
cont = 0
for i in matriz:
    for j in i:
        if j > 10:
            cont += 1
print(f'A matriz tem {cont} números maiores que 10')

# 2
pos = -1
matriz = [[], [], [], [], []]
for lista in matriz:
    while len(lista) < 5:
        lista.append(0)
for lista in matriz:
    pos += 1
    for n in lista:
        lista[pos] = 1
for lista in matriz:
    print(lista)

# 3
linha = 0
coluna = -1
matriz = [[], [], [], []]
for lista in matriz:
    while len(lista) < 4:
        coluna += 1
        lista.append(linha * coluna)
        if coluna == 3:
            coluna = -1
            linha += 1
for i in matriz:
    print(i)

# 4
from random import randrange
condicao = False
linha = -1
coluna = -1
matriz = [[], [], [], []]
aux = []
for lista in matriz:
    while len(lista) < 4:
        lista.append(randrange(0, 50))
for lista in matriz:
    maxi = max(lista)
    if maxi not in aux:
        aux.append(maxi)
maior = max(aux)
for i in matriz:
    if condicao == True:
        break
    else:
        coluna = -1
        linha += 1
        for j in i:
            coluna += 1
            if maior == j:
                condicao = True
                break

for a in matriz:
    print(a)
print(f'O maior número é {maior} e está na posição {linha}x{coluna}')

# 5
from random import randrange
linha = -1
coluna = -1
condicao = False
n = int(input('Informe um valor: '))
matriz = [[], [], [], [], []]
for i in matriz:
    while len(i) < 5:
        i.append(randrange(0, 10))
for lista in matriz:
    coluna = -1
    linha += 1
    for numero in lista:
        coluna += 1
        if numero == n:
            for a in matriz:
                print(a)
            print(f'O número {n} está na linha: {linha} x coluna: {coluna}')
            condicao = True
            break
if condicao == False:
    for a in matriz:
        print(a)
    print(f'O número {n} não foi encontrado')

# 6
matriz1 = [[1, 4, 5, 6], [8, 12, 35, 4], [0, 0, 2, 3], [6, 5, 4, 8]]
matriz2 = [[26, 4, 7, 8], [2, 6, 4, 3], [1, 2, 4, 3], [4, 8, 5, 6]]
matriz3 = [[], [], [], []]
posicao = -1
linha = -1

for lista in matriz3:
    linha += 1
    while len(lista) < 4:
        posicao += 1
        for lista_m1 in matriz1:
            n1 = matriz1[linha]
            n1 = n1[posicao]
        for lista_m2 in matriz2:
            n2 = matriz2[linha]
            n2 = n2[posicao]
        if n1 > n2:
            lista.insert(posicao, n1)
        elif n2 > n1:
            lista.insert(posicao, n2)
        else:
            lista.insert(posicao, n1)
        if posicao == 3:
            posicao = -1
for linha in matriz3:
    print(linha)

#6 com random
from random import randrange
matriz1 = [[], [], [], []]
matriz2 = [[], [], [], []]
matriz3 = [[], [], [], []]
posicao = -1
linha = -1

for lista in matriz1:
    while len(lista) < 4:
        lista.append(randrange(1, 50 + 1))
for lista in matriz2:
    while len(lista) < 4:
        lista.append(randrange(1, 50 + 1))

for lista in matriz3:
    linha += 1
    while len(lista) < 4:
        posicao += 1
        for lista_m1 in matriz1:
            n1 = matriz1[linha]
            n1 = n1[posicao]
        for lista_m2 in matriz2:
            n2 = matriz2[linha]
            n2 = n2[posicao]
        if n1 > n2:
            lista.insert(posicao, n1)
        elif n2 > n1:
            lista.insert(posicao, n2)
        else:
            lista.insert(posicao, n1)
        if posicao == 3:
            posicao = -1
for linha in matriz3:
    print(linha)
print(matriz1)
print(matriz2)

# 7
import numpy as np

matriz = np.zeros([10, 10], int)

for l in range(10):
    for c in range(10):
        if l < c:
            matriz[l][c] = (2 * l + 7 * c) - 2
        elif l == c:
            matriz[l][c] = (3 * (l ** 2)) - 1
        elif l > c:
            matriz[l][c] = (4 * (l ** 3) - 5 * (c ** 2)) + 1

print(matriz)

# 8
from random import randrange
matriz = [[], [], []]
coluna = -1
linha = -1
soma = 0
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 30 + 1))
for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        if linha == 0 and coluna == 1:
            soma += numero
        elif linha == 0 and coluna == 2:
            soma += numero
        elif linha == 1 and coluna == 2:
            soma += numero
    coluna = -1
for i in matriz:
    print(i)
print('-' * 15)
print(f'A soma dos números acima da diagonal principal é: {soma}')

# 9
from random import randrange
matriz = [[], [], []]
coluna = -1
linha = -1
soma = 0
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 30 + 1))
for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        if linha == 1 and coluna == 0:
            soma += numero
        elif linha == 2 and coluna == 0:
            soma += numero
        elif linha == 2 and coluna == 1:
            soma += numero
    coluna = -1
for i in matriz:
    print(i)
print('-' * 15)
print(f'A soma dos números abaixo da diagonal principal é: {soma}')

# 10
from random import randrange
matriz = [[], [], []]
coluna = -1
linha = -1
soma = 0
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 30 + 1))
for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        if linha == 0 and coluna == 0:
            soma += numero
        elif linha == 1 and coluna == 1:
            soma += numero
        elif linha == 2 and coluna == 2:
            soma += numero
    coluna = -1
for i in matriz:
    print(i)
print('-' * 15)
print(f'A soma dos números abaixo da diagonal principal é: {soma}')

# 11
from random import randrange
matriz = [[], [], []]
coluna = -1
linha = -1
soma = 0
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 30 + 1))
for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        if linha == 0 and coluna == 2:
            soma += numero
        elif linha == 1 and coluna == 1:
            soma += numero
        elif linha == 2 and coluna == 0:
            soma += numero
    coluna = -1
for i in matriz:
    print(i)
print('-' * 15)
print(f'A soma dos números abaixo da diagonal secundária é: {soma}')

# 12
from random import randrange
matriz = [[], [], []]
mtransp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = -1
coluna = -1
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 30+1))
for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        mtransp[coluna][linha] = numero
    coluna = -1
for a in matriz:
    print(a)
print('-' * 20)
for b in mtransp:
    print(b)

# 13

from random import randrange

matriz = [[], [], [], []]
linha = -1
coluna = -1
for a in matriz:
    while len(a) < 4:
        a.append((randrange(1, 20 + 1)))

for b in matriz:
    print(b)

matriz2 = matriz.copy()

for lista in matriz:
    linha += 1
    for numero in lista:
        coluna += 1
        if coluna > linha:
            matriz2[linha][coluna] = 0
    coluna = -1

print('-' * 20)
for c in matriz2:
    print(c)

# 14
from random import randrange
verif = False
cartela = [[], [], [], [], []]
for lista in cartela:
    while len(lista) < 5:
        n = randrange(1, 99+1)
        for linha in cartela:
            for numero in linha:
                if n == numero:
                    verif = True
        if verif == False:
            lista.append(n)
        verif = False
for i in cartela:
    print(i)

# 15
from random import randrange
alternativas = ['a', 'b', 'c', 'd']
respostas = [[], [], [], [], []]
resultados = []
gabarito = ['b', 'a', 'c', 'd', 'd', 'a', 'b', 'd', 'c', 'a']
linha = -1
coluna = -1
cont = 0

for lista in respostas:
    while len(lista) < 10:
        lista.append(alternativas[randrange(4)])
for aluno in respostas:
    linha += 1
    for letra in aluno:
        coluna += 1
        if aluno[coluna] == gabarito[coluna]:
            cont += 1
    resultados.append(cont)
    coluna = -1
    cont = 0

for a in respostas:
    print(a)
print('-' * 20)
print(f'Gabarito: {gabarito}')
print(f'Resultados: {resultados}')

# 16
import random
gabarito = ['a', 'b', 'c', 'e', 'a', 'e', 'd', 'e', 'd', 'a']
aluno1 = [[], [], []]
aluno2 = [[], [], []]
aluno3 = [[], [], []]
posicao = -1
cont = 0

for x in range(1, 4):
    matricula = int(input(f'Informe a matricula do {x}º aluno: '))
    if x == 1:
        aluno1[0].append(matricula)
        while len(aluno1[1]) < 10:
            aluno1[1].append(random.choice('abcde'))
        for resposta in gabarito:
            posicao += 1
            if gabarito[posicao] == aluno1[1][posicao]:
                cont += 1
        if cont >= 7:
            aluno1[2].append(cont)
            aluno1[2].append('APROVADO')
        else:
            aluno1[2].append(cont)
            aluno1[2].append('REPROVADO')
        posicao = -1
        cont = 0
    elif x == 2:
        aluno2[0].append(matricula)
        while len(aluno2[1]) < 10:
            aluno2[1].append(random.choice('abcde'))
        for resposta in gabarito:
            posicao += 1
            if gabarito[posicao] == aluno2[1][posicao]:
                cont += 1
        if cont > + 7:
            aluno2[2].append(cont)
            aluno2[2].append('APROVADO')
        else:
            aluno2[2].append(cont)
            aluno2[2].append('REPROVADO')
        posicao = -1
        cont = 0
    elif x == 3:
        aluno3[0].append(matricula)
        while len(aluno3[1]) < 10:
            aluno3[1].append(random.choice('abcde'))
        for resposta in gabarito:
            posicao += 1
            if gabarito[posicao] == aluno3[1][posicao]:
                cont += 1
        if cont > + 7:
            aluno3[2].append(cont)
            aluno3[2].append('APROVADO')
        else:
            aluno3[2].append(cont)
            aluno3[2].append('REPROVADO')
print('-' * 15)
print(f'Matricula:{aluno1[0]}, Respostas:{aluno1[1]}, Quantidade:{aluno1[2][0]}, Situação:{aluno1[2][1]}')
print('-' * 15)
print(f'Matricula:{aluno2[0]}, Respostas:{aluno2[1]}, Quantidade:{aluno2[2][0]}, Situação:{aluno2[2][1]}')
print('-' * 15)
print(f'Matricula:{aluno3[0]}, Respostas:{aluno3[1]}, Quantidade:{aluno3[2][0]}, Situação:{aluno3[2][1]}')
print('-' * 15)
print(f'Gabarito:                {gabarito}')

# 17
from random import randrange
from collections import Counter
notas = [[], [], [], [], [], [], [], [], [], []]
contador = []
for x in notas:
    while len(x) < 3:
        x.append(randrange(1, 10+1))
for aluno in notas:
    minimo = aluno.index(min(aluno))
    contador.append(minimo)
pior_nota = Counter(contador)
for a in notas:
    print(a)
print('-' * 20)
print(f'{pior_nota[0]} alunos tiveram a pior nota na prova 1')
print(f'{pior_nota[1]} alunos tiveram a pior nota na prova 2')
print(f'{pior_nota[2]} alunos tiveram a pior nota na prova 3')

# 18
indice = 0
matriz = [[], [], []]
lista = []
posicao = -1
p1 = 0
p2 = 0
p3 = 0
for elemento in matriz:
    indice += 1
    for i in range(3):
        n = int(input(f'Informe os números da {indice}ª lista: '))
        elemento.append(n)
for a in matriz:
    for b in a:
        posicao += 1
        if posicao == 0:
            p1 += b
        elif posicao == 1:
            p2 += b
        elif posicao == 2:
            p3 += b
    posicao = -1
lista.append(p1)
lista.append(p2)
lista.append(p3)
for c in matriz:
    print(c)
print('-' * 20)
print(lista)

# 19
indice = 0
matriz = [[], [], [], [], []]
medias = []
for elemento in matriz:
    indice += 1
    for i in range(1):
        matricula = int(input(f'Informe o numero de matricula do {indice}º aluno: '))
        elemento.append(matricula)
        np = int(input(f'Informe a média das provas do {indice}º aluno: '))
        while np < 0 or np > 10:
            print('Nota inválida')
            np = int(input(f'Informe a média das provas do {indice}º aluno: '))
        elemento.append(np)
        nt = int(input(f'Informe a média dos trabalhos do {indice}º aluno: '))
        while nt < 0 or nt > 10:
            print('Nota inválida')
            nt = int(input(f'Informe a média dos trabalhos do {indice}º aluno: '))
        elemento.append(nt)
        media = (nt + np) / 2
        elemento.append(media)
        print('-' * 20)
for lista in matriz:
    medias.append(lista[3])
maior = max(medias)
for lista in matriz:
    if lista[3] == maior:
        matricula_maior = lista[0]
for a in matriz:
    print(a)
print('-' * 20)
print(f'A maior nota final é {maior} e a matricula do aluno é {matricula_maior}')
print('-' * 20)
print(f'A média aritmética das notas finais é {sum(medias) / len(medias)}')

# 20
from random import randrange
soma_impar = 0
soma_colunas = 0
cont = 0
coluna = -1
matriz = [[], [], []]
for lista in matriz:
    while len(lista) < 6:
        lista.append(randrange(1, 20+1))
for lista in matriz:
    for numero in lista:
        coluna += 1
        if coluna % 2 != 0:
            soma_impar += numero
        if coluna == 2 or coluna == 4:
            cont += 1
            soma_colunas += numero
            media = soma_colunas / cont
    coluna = -1
for a in matriz:
    print(a)
print('-' * 20)
print(f'A soma das colunas impares é {soma_impar}')
print(f'A média aritmética dos elementos da segunda e quarta colunas é {media}')
for lista in matriz:
    lista[5] = lista[0] + lista[1]
print('-' * 20)
for a in matriz:
    print(a)

# 21
from random import randrange
matriz1 = [[], []]
matriz2 = [[], []]
res = [[0, 0], [0, 0]]
posicao = -1
linha = -1
for lista in matriz1:
    while len(lista) < 2:
        lista.append(randrange(1, 20+1))
for lista in matriz2:
    while len(lista) < 2:
        lista.append(randrange(1, 20+1))
for x in range(1):
    print(matriz1[0], end="  ")
    print(matriz2[0])
    print(matriz1[1], end="  ")
    print(matriz2[1])
print('-' * 20)
opcao = (input(f'A - Somar as duas matrizes\n'
                  f'B - Subtrair a primeira matriz da segunda\n'
                  f'C - Adicionar uma constante às duas matrizes\n'
                  f'D - Imprimir as matrizes\n'
                  f'Escolha uma opção: '))
print('-' * 20)
if opcao == 'A':
    for i in res:
        linha += 1
        for numero in i:
            posicao += 1
            res[linha][posicao] = matriz1[linha][posicao] + matriz2[linha][posicao]
        posicao = -1
    for c in res:
        print(c)
elif opcao == 'B':
    for i in res:
        linha += 1
        for numero in i:
            posicao += 1
            res[linha][posicao] = matriz1[linha][posicao] - matriz2[linha][posicao]
        posicao = -1
    for c in res:
        print(c)
elif opcao == 'C':
    print('Em breve')
elif opcao == 'D':
    for x in range(1):
        print(matriz1[0], end="  ")
        print(matriz2[0])
        print(matriz1[1], end="  ")
        print(matriz2[1])

# 22
from random import randrange
matriz_a = [[], [], []]
matriz_b = [[], [], []]
matriz_c = [[], [], []]
linha = -1
coluna = -1

for a in matriz_a:
    while len(a) < 3:
        a.append(randrange(1, 20+1))
for a in matriz_b:
    while len(a) < 3:
        a.append(randrange(1, 20+1))
for lista in matriz_a:
    linha += 1
    for numero in lista:
        coluna += 1
        matriz_c[linha].append(matriz_a[linha][coluna] * matriz_b[linha][coluna])
    coluna = -1
for a in matriz_a:
    print(a)
print('-' * 15)
for a in matriz_b:
    print(a)
print('-' * 15)
for a in matriz_c:
    print(a)

# 23
from random import randrange
matriz_a = [[], [], []]
matriz_b = [[], [], []]
linha = -1
coluna = -1
for a in matriz_a:
    while len(a) < 3:
        a.append(randrange(1, 20+1))
for lista in matriz_a:
    linha += 1
    for numero in lista:
        coluna += 1
        matriz_b[linha].append(matriz_a[linha][coluna] * matriz_a[linha][coluna])
    coluna = -1
for a in matriz_a:
    print(a)
print('-' * 15)
for a in matriz_b:
    print(a)

# 24
matriz = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
          [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
          [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
          [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
          [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
          [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
          [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
          [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
          [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
          [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
          [78, 1, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
          [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
          [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
          [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
          [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
          [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
          [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
          [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
          [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
          [61, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

maximos = []
direita = []
for n in range(20):
    for m in range(20):
        if m + 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n][m + 1] * matriz[n][m + 2] * matriz[n][m + 3]
            direita.append(multiplicacao)
            if multiplicacao == max(direita):
                linhad = n
                colunad = m
maximos.append(max(direita))

esquerda = []
for n in range(20):
    for m in range(20):
        if m - 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n][m - 1] * matriz[n][m - 2] * matriz[n][m - 3]
            esquerda.append(multiplicacao)
            if multiplicacao == max(esquerda):
                linhaE = n
                colunaE = m
maximos.append(max(esquerda))

cima = []
for n in range(20):
    for m in range(20):
        if n + 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n + 1][m] * matriz[n + 2][m] * matriz[n + 3][m]
            cima.append(multiplicacao)
            if multiplicacao == max(cima):
                linhaC = n
                colunaC = m
maximos.append(max(cima))

baixo = []
for n in range(20):
    for m in range(20):
        if n + 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n - 1][m] * matriz[n - 2][m] * matriz[n - 3][m]
            baixo.append(multiplicacao)
            if multiplicacao == max(baixo):
                linhaB = n
                colunaB = m
maximos.append(max(baixo))

Diagonal1 = []
for n in range(20):
    for m in range(20):
        if n + 3 < 20 and m + 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n + 1][m + 1] * matriz[n + 2][m + 2] * matriz[n + 3][m + 3]
            Diagonal1.append(multiplicacao)
            if multiplicacao == max(Diagonal1):
                linhaD1 = n
                colunaD1 = m
maximos.append(max(Diagonal1))

diagonal2 = []
for n in range(20):
    for m in range(20):
        if n - 3 < 20 and m - 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n - 1][m - 1] * matriz[n - 2][m - 2] * matriz[n - 3][m - 3]
            diagonal2.append(multiplicacao)
            if multiplicacao == max(diagonal2):
                linhaD2 = n
                colunaD2 = m
maximos.append(max(diagonal2))

diagonal3 = []
for n in range(20):
    for m in range(20):
        if n + 3 < 20 and m - 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n + 1][m - 1] * matriz[n + 2][m - 2] * matriz[n + 3][m - 3]
            diagonal3.append(multiplicacao)
            if multiplicacao == max(diagonal3):
                linhaD3 = n
                colunaD3 = m
maximos.append(max(diagonal3))

diagonal4 = []
for n in range(20):
    for m in range(20):
        if n - 3 < 20 and m + 3 < 20:
            multiplicacao = matriz[n][m] * matriz[n - 1][m + 1] * matriz[n - 2][m + 2] * matriz[n - 3][m + 3]
            diagonal4.append(multiplicacao)
            if multiplicacao == max(diagonal4):
                linhaD4 = n
                colunaD4 = m
maximos.append(max(diagonal4))

print(maximos)
print(max(maximos))
print(linhaD3, colunaD3)

# 25
tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
resultado = False
contador = 0
controle_x = 0
controle_o = 0

while resultado != True:
    for a in tabuleiro:  # Exibir o tabuleiro
        print(a)
    print('-' * 15)

    if contador % 2 == 0:  # Jogada do jogador 1
        linha = int(input('Jogador 1 - Insira posiçao \n'
                          'Linha (0 a 2): '))
        coluna = int(input('Coluna (0 a 2): '))
        if tabuleiro[linha][coluna] != ' ':
            print('Jogada inválida!')
            print('-' * 15)
        else:
            tabuleiro[linha][coluna] = 'X'
            contador += 1
            print('-' * 15)

    else:  # Jogada do jogador 2
        linha = int(input('Jogador 2 - Insira posiçao \n'
                          'Linha (0 a 2): '))
        coluna = int(input('Coluna (0 a 2): '))
        if tabuleiro[linha][coluna] != ' ':
            print('Jogada inválida!')
            print('-' * 15)
        else:
            tabuleiro[linha][coluna] = 'O'
            contador += 1
            print('-' * 15)

    # Possibilidades de Vitória
    vitoria = [
        [tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]],
        [tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]],
        [tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]],
        [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
        [tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]],
        [tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]],
        [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
        [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]
    ]

    # Verificando se houve vitória
    for lista in vitoria:
        controle_x = 0
        controle_o = 0
        for possibilidade in lista:
            if possibilidade == 'X':
                controle_x += 1
                if controle_x == 3:
                    print('Jogador 1 ganhou !\n'
                          f'Quantidade de jogadas: {contador}')
                    resultado = True
                    break
            elif possibilidade == 'O':
                controle_o += 1
                if controle_o == 3:
                    print('Jogador 2 ganhou !\n'
                          f'Quantidade de jogadas: {contador}')
                    resultado = True
                    break
            if contador == 9 and not resultado:
                print('Deu velha!')
                resultado = True

    if resultado == True:
        for a in tabuleiro:
            print(a)
"""



