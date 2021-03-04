"""
# 1
lista = []
for n in range(1, 50):
    if n % 3 == 0:
        lista.append(n)
print(lista[0:3])

# 2
num = range(1, 101)

for vez in range(3):
    for n in num:
        print(n)

# 3
n = 11
while n > 0:
    n = n - 1
    print(n)
    if n == 0:
        print('FIM')

# 4
cont = 540
while cont < 100_000:
    print(cont)
    cont = cont + 1000

# 5
soma = 0
cont = 0
while cont < 10:
    cont += 1
    n = int(input(f'{cont}/10   Digite um número: '))
    soma = n + soma
print(soma)

# 6
soma = 0
cont = 0
for n in range(1, 11):
    cont += 1
    n = int(input(f'{cont}/10   Digite um número: '))
    soma = n + soma
    media = soma/10
print(media)

# 7
descarte = []
cont = 0
soma = 0
while cont < 10:
    cont += 1
    n = int(input(f'{cont}/10   Informe um valor inteiro: '))
    if n < 0:
        descarte.append(n)
    else:
        soma = soma + n
media = soma / (10-len(descarte))
print(media)
print(soma)
print(len(descarte))

# 8
cont = 0
lista = []

while cont < 10:
    cont += 1
    n = int(input(f'{cont}/10   Informe um valor inteiro: '))
    lista.append(n)
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

# 9
num = int(input("Digite um número inteiro: "))

for n in range(1, num + num, 2):
    print(n)

# 10
n = 0
soma = 0
for n in range(0, 101, 2):
    soma = n + soma
print(soma)

# 11
cont = 0
n = int(input('Imprimir até qual número? (positivo) : '))
if n < 0:
    print('Número positivo, por favor')
else:
    for i in range(cont, n):
        cont += 1
        print(cont)

# 12
n = int(input('De qual número começar? : '))
for n in range(n+1, 0, -1):
    n -= 1
    print(n)

# 13
n = int(input('Imprimir até qual número(par): '))
if n % 2 != 0 or n < 0:
    print('Informe um número positivo/par')
else:
    for i in range(2, n+1, 2):
        print(i)

# 14
n = int(input('Imprimir a partir de qual número(par): '))
if n % 2 != 0 or n < 0:
    print('Informe um número positivo/par')
else:
    for i in range(n, -2, -2):
        print(i)

# 15
n = int(input('Imprimir até qual número(impar): '))
if n % 2 != 1 or n < 0:
    print('Informe um número positivo/impar')
else:
    for i in range(1, n+1, 2):
        print(i)

# 16
n = int(input('Imprimir a partir de qual número(impar): '))
if n % 2 != 1 or n < 0:
    print('Informe um número positivo/par')
else:
    for i in range(n, 0, -2):
        print(i)

# 17
soma = 0
n = int(input('Somar até qual número?: '))
for i in range(0, n+1):
    soma = soma+i
print(soma)

# 18
numeros = []
qtd = int(input('Quantos números deseja inserir? : '))
for i in range(0, qtd):
    n = int(input(f'Informe o {i+1}º número: '))
    numeros.append(n)

print(f'Maior número: {max(numeros)}')
print(f'Números de ocorrência: {numeros.count((max(numeros)))}')

# 19
n = input('Informe um número entre 100 e 999: ')
nn = int(n)
if nn < 100 or nn > 999:
    print('Número inválido')
else:
    for i in n:
        print(i)

# 20
geral = []
pares = []
n = 0
while n != 1000:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'{n} é par')
        pares.append(n)
        geral.append(n)
    else:
        print(f'{n} é impar')
        geral.append(n)

print(f'Quantidade de números lidos: {len(geral)}')
print(f'Quantidade de números pares: {len(pares)}')

# 21
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
produto = 1
pares = []
impares = []

for i in range(n1, n2+1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
for j in impares:
    produto = j * produto
print(f'Soma dos pares: {sum(pares)}')
print(f'Multiplicação dos impares: {produto}')

# 22
nota = 10
notas = []
while nota >= 10 and nota <= 20:
    nota = int(input('Informe as notas: '))
    if nota < 10 or nota > 20:
        break
    else:
        notas.append(nota)
if len(notas) == 0:
    print('Deverá ter pelo menos 1 nota válida')
else:
    print(f'Média aritmética: {sum(notas)/len(notas)}')

# 23
n = int(input('Informe um número: '))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# 24
soma = 0
n = int(input('Informe um número inteiro: '))
for i in range(1, n):
    if n % i == 0:
        soma += i
print(soma)

# 25
soma = 0
for i in range(1, 1000):
    if i % 5 == 0 or i % 3 == 0:
        soma += i
print(f'O resultado da soma é: {soma}')

# 26
n = int(input('Informe um número: '))
for i in range(n+1, n+17):
    if i % 11 == 0:
        print(f'{i} é divisível por 11')
        break
    elif i % 13 == 0:
        print(f'{i} é divisível por 13')
        break
    elif i % 17 == 0:
        print(f'{i} é divisível por 17')
        break

# 27
termos = int(input('Informe a quantidade de termos: '))
h = 1
for n in range(1, (termos + 1)):
    h = h + (1 / (n + 1))

print(f'H{termos} vale {h}')

# 28
import math

soma = 1

numero = int(input("Digite um número: "))

while numero <= 0:
    print("Você deve digitar um número maior do que 0 (zero)!")
    numero = int(input("Digite um número: "))
for n in range(numero, 0, -1):
    soma = soma + (1 / math.factorial(n))
print(f'\nO resultado de E para N = {numero} é >>>> {soma:.5f}.')

# 29
from math import factorial
f, numerador = 1, 0
n = 0
cont = 1
s = 0
while cont <= 5:
    n = n + 2  # denumerador vai ser sempre um numero par até 10
    f = factorial(n)
    numerador = numerador + 1
    s = (numerador / f) + s
    cont = cont + 1
    print(f'{numerador}/{f} = {s:.2f}')
print(f'o valor final de S é: {s}')

# 30
n = int(input('Informe até qual número vai a sequencia: '))
soma = 0
res = 0
soma2 = 0
for i in range(1, n+1):
    soma += i
print(f'Primeira sequência: {soma}')
for i in range(1,n+1):
    if i % 2 == 0:
        res -= i
    else:
        res += i
print(f'Segunda sequência: {res}')
for i in range(1, n+1, 2):
    soma2 += i
print(f'Terceira sequência: {soma2}')

# 31
soma = 0
c = 0
for i in range(1, 100, +2):
    c += 1
    soma += i / c
print(soma)

# 32
import random, time

n = int(input('Quantas vezes quer jogar o dado: '))
for i in range(1, n+1):
    time.sleep(1)
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    if d1 == d2:
        print(f'Dado 1: {d1} = {d2}: Dado 2')
    elif d1 > d2:
        print(f'Dado 1: {d1} > {d2}: Dado 2')
    else:
        print(f'Dado 1: {d1} < {d2}: Dado 2')

# 33
qtdd = int(input('Digite a quantidade de multiplos: '))
i = int(input('Digite i: '))
j = int(input('Digite j: '))
n = 0
lista1 = []

while len(lista1) < qtdd:
    if n % i == 0:
        lista1.append(n)
    elif n % j == 0:
        lista1.append(n)
    n += 1
print(f'A lista dos multiplos de i e j ou dos 2 é: {lista1}')

# 34
n = 1

while True:
    check = 0
    for i in range(1, 11):  # loop para construir o valor a ser checado
        check += n % i

    if check == 0:
        print(f'O menor divisível é: {n}.')
        break
    n += 1

# 35
n1 = int(input('Informe o valor inicial: '))
n2 = int(input('Informe o valor final: '))
soma = 0

if n1 > n2:
    print('Intervalo de valores inválido')
else:
    for i in range(n1, n2+1):
        if i % 2 != 0:
            soma += i
print(soma)

# 36
res2 = 0
res = 0
for i in range(1, 101):
    res += i*i
for i in range(1, 101):
    res2 += i
print(f'A soma dos quadrados dos cem primeiros números naturais é: {res}')
print(f'O quadrado da soma dos cem primeiros números naturais é {res2*res2}')
print('A diferença entre a soma dos quadrados dos cem primeiros números naturais'
      f'e o quadrado da soma é {(res2*res2)-res}')

# 37
res = 0
for i in range(1000, 9999+1):
    a = str(i)
    b = int(a[0:2])
    c = int(a[2:4])
    res = (b+c)*(b+c)
    if res == i:
        print(i)

# 38
for a in range (1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if (a+b+c) == 1000:
                if (a ** 2 + b ** 2) == c ** 2:
                    print(f'{a},{b},{c}')

# 39
a = 0
b = 0
while a <= 0 or b <= 0:
    b = int(input('Informe a base do triângulo: '))
    a = int(input('Informe a altura do triângulo: '))
area = (b * a) / 2
print(area)

# 40
lista = []
num = int(input('Insira um número: '))
while num >= 0:
    lista.append(num)
    num = int(input('Insira um número: '))
    if num < 0:
        break
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

# 41
r1 = True
r2 = True
while r1 != 0 or r2 != 0:
    r1 = int(input('Informe o valor de r1:'))
    r2 = int(input('Informe o valor de r2:'))
    if r1 == 0 or r2 == 0:
        print('Programa encerrado')
        break
    else:
        res = (r1 * r2) / (r1 + r2)
        print(res)

# 42
import math
n = True
while n > 0:
    n = int(input('Informe o valor para saber o n², n³ e raiz quadrada:'))
    if n <= 0:
        print('Programa encerrado')
        break
    else:
        print(f'Número ao quadrado: {n*n}')
        print(f'Número ao cubo: {n*n*n}')
        print(f'Raiz quadrada: {math.sqrt(n)}')

# 43
idade = 1
idades = []
while idade > 0:
    if idade <= 0:
        break
    else:
        idade = int(input('Informe a idade: '))
        idades.append(idade)

print(f'Média das idades: {sum(idades)/len(idades)}')

# 44
lista = []
n = int(input('Informe até onde calcular a sequência de Fibonacci: '))
soma = 0
while soma < n:
    if soma == 0:
        lista.append(soma)
        soma += 1
        lista.append(soma)
    else:
        soma = lista[-1] + lista[-2]
        lista.append(soma)
print(lista)

# 45

n = True
while n != 0:
    n = float(input('1 - km/h para m/s\n'
                    '2 - m/s para km/h\n'
                    '0 - sair\n'
                    'Informe o que deseja calcular: '))
    if n < 0 or n > 2:
        print('Valor inválido')
    elif n == 1:
        km = float(input('Informe os km/h: '))
        mps = km/3.6
        print(f'{km}km/h = {mps}m/s')
        print('-'*30)
    elif n == 2:
        mps = float(input('Informe os m/s: '))
        km = mps * 3.6
        print(f'{mps}m/s = {km}km/h')
        print('-'*30)
    else:
        print('Programa encerrado')

# 46
import random
tentativas = 0
while True:
    n1 = random.randrange(1, 1001)
    n2 = int(input('Adivinhe o número entre 1 e 1000: '))
    if n1 != n2 and n1 > n2:
        print('O número informado é menor que o sorteado')
        print('-' * 30)
        tentativas += 1
    elif n1 != n2 and n1 < n2:
        print('O número informado é maior que o sorteado')
        print('-' * 30)
        tentativas += 1
    else:
        tentativas += 1
        print(f'Acertou! \n'
              f'Foram necessárias {tentativas} tentativas')
        break

# 47
while True:
    escolha = int(input('1 - Adição\n'
                        '2 - Subtração\n'
                        '3 - Multiplicação\n'
                        '4 - Divisão\n'
                        '5 - Saída\n'
                        'Escolha a operação: '))
    if escolha < 1 or escolha > 5:
        print('Opção inválida')
        print('-' * 30)
    elif escolha == 5:
        print('Programa encerrado')
        break
    else:
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
        if escolha == 1:
            print(f'Resultado: {n1 + n2}')
            print('-' * 30)
        elif escolha == 2:
            print(f'Resultado: {n1 - n2}')
            print('-' * 30)
        elif escolha == 3:
            print(f'Resultado: {n1 * n2}')
            print('-' * 30)
        elif escolha == 4:
            print(f'Resultado: {n1 / n2}')
            print('-' * 30)

# 48
lista = []
lista_p = []
soma = 0
while soma < 4_000_000:
    lista.append(soma)
    if soma % 2 == 0:
        lista_p.append(soma)
    if soma == 0:
        soma += 1
        lista.append(soma)
    else:
        soma = lista[-1] + lista[-2]
print(sum(lista_p))

# 49
meses = 0
s_carlos = float(input('Informe o salário de Carlos: R$'))
s_joao = s_carlos / 3
while s_joao <= s_carlos:
    s_carlos += (s_carlos * 2) / 100
    s_joao += (s_joao * 5) / 100
    meses += 1
print(f'O investimento de João demorará {meses} meses para ultrapassar o de Carlos')

# 50
anos = 0
altura1 = 1.50
altura2 = 1.10
while altura2 < altura1:
    altura1 = altura1 + 0.02
    altura2 = altura2 + 0.03
    anos += 1
print(f'São necessários {anos} anos para Chico ultrapassar Zé')
print('Chico '"%.2f" % altura1)
print('Zé ' "%.2f" % altura2)

# 51
ano_contratacao = 1995
salario = 2000.0
ano_atual = 2021
porcentagem = 1.5
porcentagem_ant = 0

while ano_contratacao < ano_atual:
    ano_contratacao += 1
    if ano_contratacao == 1996:
        salario += (salario * porcentagem) / 100
        porcentagem_ant = porcentagem
    else:
        porcentagem = porcentagem_ant * 2
        salario += (salario * porcentagem) / 100
        porcentagem_ant = porcentagem
print(f'O salário atual é R${salario:.2f}')

# 52
saque = float(input('Informe o valor do saque: R$'))
v = 0.0
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
lista = []

while True:
    if (saque - v) >= 100 and (v + 100) <= saque:
        v += 100.00
        n100 += 1
        lista.append(100)
    elif (saque - v) >= 50 and (v + 50) <= saque:
        v += 50.00
        n50 += 1
        lista.append(50)
    elif (saque - v) >= 20 and (v + 20) <= saque:
        v += 20.00
        n20 += 1
        lista.append(20)
    elif (saque - v) >= 10 and (v + 10) <= saque:
        v += 10.00
        n10 += 1
        lista.append(10)
    elif (saque - v) >= 5 and (v + 5) <= saque:
        v += 5
        n5 += 1
        lista.append(5)
    elif (saque - v) >= 2 and (v + 2) <= saque:
        v += 2
        n2 += 1
        lista.append(2)
    elif (saque - v) >= 1 and (v + 1) <= saque:
        v += 1
        n1 += 1
        lista.append(1)
    elif (saque - v) == 0:
        break
print(lista)

# 53
n = 0
linhas = int(input('Digite a quantidade de linhas:'))
for i in range(1, linhas+2):
    for j in range(1, i):
        n = n + 1
        print(n, end=' ')
    print('')

# 54
divisores = []
n = int(input('Informe um número positivo maior que 1: '))
while n < 2:
    n = int(input('Informe um número positivo maior que 1: '))
for i in range(1, n+1):
    if n % i == 0:
        divisores.append(i)
if len(divisores) == 2 and divisores.__contains__(1) and divisores.__contains__(n):
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
print(divisores)

# 55
print('Este programa recebe um inteiro n e retorna a soma dos n primeiros números primos.')

n = int(input('Inteiro: '))
count = 0  # variável para contar o número de primos
i = 1  # valor do número a ser verificado
soma = 0

while count < n:
    check_primo = True  # variável que informa se i é primo ou não

    for j in range(1, i + 1):  # loop para verificar se i é primo
        if i % j == 0 and j != i and j != 1:
            check_primo = False
            break

    if check_primo:
        if count == 0:
            print('Primos: ', end='')

        if count == n - 1:
            print(i)
        else:
            print(i, end=', ')
        count += 1
        soma += i
    i += 1

print(f'\nA soma dos {n} primeiros números primos é: {soma}.')

# 56
from tqdm import tqdm
soma = 0
primos = []

for i in tqdm(range(1, 2_000_000 + 1)):
    cont = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        primos.append(i)
print(sum(primos))

# 57
inicial = int(input('Informe o número inicial: '))
final = int(input('Informe o número final: '))
soma = 0
for i in range(inicial, final + 1):
    cont = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        soma += i
print(f'A soma dos números primos entre {inicial} e {final} é: {soma}')

# 58
inicial = int(input('Informe o número inicial: '))
final = int(input('Informe o número final: '))
soma = 0
for i in range(inicial, final + 1):
    cont = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        soma += 1
print(f'A contagem dos números primos entre {inicial} e {final} é: {soma}')


# 59
soma1 = 0
soma2 = 0
soma3 = 0
lista = []
hab = int(input('Digite o número de habitantes: '))
for c in range(1, hab + 1):
    print('\nOPÇÕES''\n[1] Residencial''\n[2] Comercial''\n[3] industrial')
    tip_cons = int(input(f'Para o habitante número {c}, qual o tipo de consumidor ele é?: '))
    if tip_cons == 1:
        kwh1 = float(input('Qual o consumo deste habitante: '))
        soma1 = soma1 + kwh1
        lista.append(kwh1)
    if tip_cons == 2:
        kwh2 = float(input('Qual o consumo deste habitante: '))
        soma2 = soma2 + kwh2
        lista.append(kwh2)
    if tip_cons == 3:
        kwh3 = float(input('Qual o consumo deste habitante: '))
        soma3 = soma3 + kwh3
        lista.append(kwh3)
print(f'O menor consumo entre todos os habitante: {min(lista):.2f}')
print(f'O maior consumo entre todos os habitantes: {max(lista):.2f}')
print(f'A média do consumo de todos os habitantes: {(soma1 + soma2 + soma3) / 3:.2f}')
print(f'A soma do consumo das Residências: {soma1:.2f}')
print(f'A soma do consumo dos Comércios: {soma2:.2f}')
print(f'A soma do consumo das industrias: {soma3:.2f}')

# 60
lista = []
cont = 0
soma = 0
while True:
    n = int(input('Informe um número: '))
    if n % 2 == 0 and n != 0:
        cont += 1
        soma += n
    if n != 0:
        lista.append(n)
    else:
        print('-' * 50)
        print(f'Soma: {sum(lista)}\n'
              f'Quantidade: {len(lista)}\n'
              f'Média: {sum(lista) / len(lista)}\n'
              f'Maior: {max(lista)}\n'
              f'Menor: {min(lista)}\n'
              f'Média números pares {soma / cont}\n'
        break

# 61
lista = []
for i in range(1, 999 + 1):
    for j in range(1, 999 + 1):
        res = i * j
        res1 = str(res)
        res1 = res1[::-1]
        res1 = int(res1)
        if res1 == res:
            lista.append(res)
print(max(lista))

# 62
from num2words import num2words

print(
    'Total de letras em um intervalo de 1 a 1000 =',
    sum(map(lambda x: len(x.replace(' ', '')), [num2words(n, lang='pt_BR') for n in range(1, 1001)]))
)
"""







