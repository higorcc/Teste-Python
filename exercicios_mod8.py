"""
# 1
def calcula_dobro(num):
    return num + num

# 2
def data(dia, mes, ano):
    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return 'Data inválida'
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'Julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Setembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    elif mes == 12:
        mes = 'Dezembro'
    return f'{dia} de {mes} de {ano}'

# 3
num = int(input('Informe um número para verificar se é positivo ou negativo: '))
def verificar():
    global num
    if num > 0:
        return f'{num} é positivo'
    elif num < 0:
        return f'{num} é negativo'
    return f'O número é {num}'

# 4
def quadrado_perfeito(num):
    for numero in range(1, num+1):
        res = numero * numero
        if res == num:
            return f'{num} é o quadrado perfeito de {numero}'
    return f'{num} não é um quadrado perfeito de outro número'

# 5

# 6
def contar_segundos(horas, minutos, segundos):
    res = 0
    for a in range(1, horas+1):
        res += 3600
    for b in range(1, minutos+1):
        res += 60
    res += segundos
    return f'{horas}:{minutos}:{segundos} = {res} segundos'

# 7
def celsius_f(c):
    f = 0
    f = c * (9.0 / 5.0) + 32.0
    return f

# 8
import math

def hipotenusa(a, b):
    res = math.sqrt((a *a) + (b * b))
    return res

# 9
def calcular_volume(altura, raio):
    volume = 3.141592 * (raio * raio) * altura
    return volume

print(calcular_volume(8, 6.8))

# 10
def maior_num(num1, num2):
    if num1 > num2:
        return f'{num1} é o maior número'
    elif num2 > num1:
        return f'{num2} é o maior número'
    return 'Os números são iguais'

# 11
def calc_nota(n1, n2, n3, tipo_media):
    media = 0
    if tipo_media.title() == 'A':
        media = f'Média: {(n1 + n2 + n3) / 3}'
        return media
    elif tipo_media.title() == 'P':
        media = f'Média: {((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10}'
        return media
    return f'Tipo de média inválido - Insira "A" ou "P"'

# 12
def contar(num):
    soma = 0
    num = str(num)
    num = num.split()
    for a in num:
        for b in a:
            b = int(b)
            soma += b
    return soma

# 13
def operacao(n1, n2, sinal):
    res = 0
    if sinal == '+':
        res = n1 + n2
        return res
    elif sinal == '-':
        res = n1 - n2
        return res
    elif sinal == '/':
        res = n1 / n2
        return res
    return 'Operação inválida'

# 14
def litros_por_km(km, litros):
    res = km / litros
    if res < 8:
        return f'{res} - Venda o carro'
    elif res >= 8 and res <= 11:
        return f'{res} - Econômico'
    return f'{res} - Super econômico'

# 15
def triangulo(lado1, lado2, lado3):
    if lado1 < 1 or lado2 < 1 or lado3 < 1:
        return 'Todos os lados devem ser positivos'
    elif lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
        return 'As medidas informadas não formam um triângulo'
    elif lado1 == lado2 == lado3:
        return 'O triângulo é equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'O triângulo é isósceles'
    return 'O triângulo é escaleno'

# 16
def desenha_linha(repeticao):
    print('=' * repeticao)

# 17
def contador(n1, n2):
    soma = 0
    for numero in range(n1 + 1, n2):
        soma += numero
    return soma

# 18
def exponenciacao(x, z):
    res = 1
    for numero in range(1, z + 1):
        res *= x
    return res

# 19
def maior_fator_primo(n):
    fator_primo = []
    i = 2

    while i <= n:
        if n % i == 0:
            fator_primo.append(i)  # exemplo se n=10, então 10 % 2 = 0. Adiciona i ao vetor
            n /= i  # atribui novo valor a n. Se n = 10, então novo valor será 5
        else:
            i += 1  # mod de 5 por 2 é diferente de 0, então atribui novo valor a i e assim sucessivamente.

    return max(fator_primo)


print(maior_fator_primo(16))

# 20
def fatorial(n):
    for numero in range(n - 1, 1, -1):
        n *= numero
    return n

# 21
def primos(num):
    lista = []
    cont = 0
    for numero in range(1, num):
        for divisor in range(1, num):
            if numero % divisor == 0:
                cont += 1
        if cont == 2:
            lista.append(numero)
        cont = 0
    return f'Os números primos até {num} são {lista}'


# 22
def exclamacao(repetir):
    for numero in range(1, repetir + 1):
        print('!' * numero)

# 23
def triangulo_lateral(tam):
    remover = 1
    for quantidade in range(1, ((tam + 1) * 2) - 1):
        if quantidade <= tam:
            print('*' * quantidade)
        else:
            print('*' * (tam - remover))
            remover += 1

# 24
def triangulo(total):
    quant = 1
    cont = 1
    for linha in range(1, total+1):
        print(' ' * (total - cont), '*' * quant)
        quant += 2
        cont += 1


# 25

# 26
def somatoria(n):
    soma = 0
    for numero in range(1, n+1):
        soma += numero
    return soma

# 27 a 31 foda-se

# 32
def simplifica(numerador, denominador):
    maior = 0
    for i in range(1, denominador):
        if numerador % i == 0 and denominador % i == 0:
            maior = i
    return f'A fração simplificada é {numerador / maior}/ {denominador / maior}'

# 33
def somar_algarismos(num):
    lista = []
    num = str(num)
    for a in num:
        lista.append(int(a))
    return sum(lista)

# 34
def fatorial_duplo(num):
    res = 1
    if num % 2 == 0 or num < 1:
        return 'O número deverá ser positivo e impar'
    else:
        for numero in range(1, num + 1, 2):
            res *= numero
    return res

# 35

# 36
def super_fatorial(num):
    mult = 1
    res = 1
    lista = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            res *= j
        lista.append(res)
        res = 1
    for numero in lista:
        mult *= numero
    return mult

# 37 e 38

# 39
def troca(a, b):
    aux = a
    a = b
    b = aux
    return f'Valores trocados: {a} - {b}'

# 40
from random import randrange
lista = []
for i in range(1, 10+1):
    lista.append(randrange(1, 10))
def contar_pares():
    cont = 0
    global lista
    for numero in lista:
        if numero % 2 == 0:
            cont += 1
    return cont

# 41
from random import randrange
lista = []
for i in range(1, 10+1):
    lista.append(randrange(1, 10))
def maior_valor():
    global lista
    return max(lista)

# 42
from random import randrange
def media_vetor():
    vetor = []
    while len(vetor) < 10:
        num = randrange(1, 15)
        vetor.append(num)
    return sum(vetor) / len(vetor)

# 43
from random import randrange
def preencher_vetor():
    vetor = []
    while len(vetor) < 10:
        num = randrange(1, 15)
        if num not in vetor:
            vetor.append(num)
    return vetor

# 44
from random import randrange
def par_impar(lista):
    a = []
    b = []
    for numero in lista:
        if numero % 2 == 0:
            a.append(numero)
        else:
            b.append(numero)
    return a, b

# 45

# 46
from random import randrange
lista = []
def imp_normal(vetor):
    return vetor

def imp_inversa(vetor):
    return vetor[::-1]

def imp_media(vetor):
    return sum(vetor) / len(vetor)

for a in range(1, 10+1):
    num = randrange(1, 50)
    lista.append(num)

opcao = input(f'1 - Imprimir o vetor na ordem normal\n'
              f'2 - Imprimir o vetor na ordem reversa\n'
              f'3 - Imprimir a média\n'
              f'Escolha: ')

if opcao == '1':
    print(imp_normal(lista))
elif opcao == '2':
    print(imp_inversa(lista))
elif opcao == '3':
    print(imp_media(lista))
else:
    print('Opcao inválida')
print(f'Lista normal: {lista}')

# 47
from random import randrange
matriz = [[], [], [], []]
for lista in matriz:
    while len(lista) < 4:
        lista.append(randrange(1, 20))

def maior_dez(matriz):
    cont = 0
    for a in matriz:
        for b in a:
            if b > 10:
                cont +=1
    return f'Há {cont} números maiores que 10 na matriz'

# 48
from random import randrange
matriz = [[], [], []]
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 20))

def diag_prin(matriz):
    return matriz[0][1] + matriz[0][2] + matriz[1][2]

print(diag_prin(matriz))
for a in matriz:
    print(a)

# 49
from random import randrange
matriz = [[], [], []]
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 20))

def diag_princ2(matriz):
    return matriz[1][0] + matriz[2][0] + matriz[2][1]

# 50
from random import randrange
matriz = [[], [], []]
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 20))

def diag_princ3(matriz):
    return matriz[0][0] + matriz[1][1] + matriz[2][2]

# 51
from random import randrange
matriz = [[], [], []]
for lista in matriz:
    while len(lista) < 3:
        lista.append(randrange(1, 20))

def diag_sec(matriz):
    return matriz[0][2] + matriz[1][1] + matriz[2][0]

# 52
from random import randrange
def matriz_transp(quantidade):
    linha = -1
    coluna = -1
    matriz = []
    while len(matriz) < quantidade:
        matriz.append([])

    for lista in matriz:
        while len(lista) < quantidade:
            lista.append(randrange(1, 25))

    print('Matriz original: ')
    for a in matriz:
        print(a)
    print('-' * 40)

    matriz2 = []
    while len(matriz2) < len(matriz):
        matriz2.append([])

    for lista in matriz:
        linha += 1
        for numero in lista:
            coluna += 1
            matriz2[coluna].insert(linha, matriz[linha][coluna])
        coluna = -1

    print('Matriz transposta:')
    for b in matriz2:
        print(b)
"""

import random


def matriz(n):
    matriz = []
    cont = 0
    controle = 'Não é uma Matriz Identidade'
    for linha in range(n):
        matriz.append([0 * n] * n)
        for coluna in range(n):
            matriz[linha][coluna] = random.randint(1, 2)
            if linha == coluna and matriz[linha][coluna] == 1:
                cont += 1
                if cont == n:
                    controle = 'Matriz Identidade'
            print(f"[{matriz[linha][coluna]:^5}]", end='')
        print()
    print("===" * 40)
    print(controle)


matriz(int(input("Insira a ordem da matriz quadrada\n")))

