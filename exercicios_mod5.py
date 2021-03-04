"""
# 1
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O número maior é: {n1}')
elif n1 == n2:
    print(f'Os números são iguais')
else:
    print(f'O número maior é: {n2}')

# 2
import math
n1 = int(input('Informe um número: '))
if n1 > 0:
    print(math.sqrt(n1))
else:
    print('O número não é válido')

# 3
import math
n = int(input('Digite um número: '))
if n >= 0:
    print(math.sqrt(n))
else:
    print(n*n)

# 4
import math

n = int(input('Digite um número: '))
if n >= 0:
    print(f'Ao quadrado: {n*n}')
    print(f'Raiz quadrada: {math.sqrt(n)}')

# 5
n = int(input('Informe um número e descubra se é par ou impar:'))
if n % 2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é impar')

# 6
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
diferença = 0
if n1 > n2:
    print(f'O número maior é: {n1}')
    print(f'A diferença é de: {n1-n2}')
elif n1 == n2:
    print(f'Os números são iguais')
else:
    print(f'O número maior é: {n2}')
    print(f'A diferença é de: {n2-n1}')

# 7
# Já fiz no 1 e 6 =)

# 8
n1 = int(input('Digite a primeira nota: '))
if n1 < 0 or n1 > 10:
    print('A nota não é válida')
else:
    n2 = int(input('Digite a segunda nota: '))
    if n2 < 0 or n2 > 10:
        print('A nota não é válida')
    else:
        print((n1+n2)/2)

# 9
salario = float(input('Informe o salário: R$'))
prestacao = float(input('Informe o valor da prestação: R$'))
if prestacao > (20*salario)/100:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')

# 10
altura = float(input('Informe a altura: '))
sexo = input('Informe o sexo (M) - (F): ')

if sexo == 'F':
    print(f'O peso ideal é {(62.1*altura)-44.7:.2f}kg')
elif sexo == 'M':
    print(f'O peso ideal é {(72.7*altura)-58:.2f}kg')
else:
    print('O valor não é valido')

# 11
num = int(input('Digite um numero de (0 a 999): '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
if num < 0:
    print('Numero invalido!')
else:
    print(f'A soma dos numeros foi {unidade} + {dezena} + {centena} = {unidade + dezena + centena}')

# 12
import math
n = int(input('Digite um numero: '))
if n > 0:
    print(math.log(n))
else:
    print('Número invalido')

# 13
av1 = float(input('Digite a primeira nota: '))
av2 = float(input('Digite a segunda nota: '))
av3 = float(input('Digite a terceira nota: '))*2
media = (av1+av2+av3)/4
if media > 6:
    print(f'Aprovado! Média: {media}')
else:
    print(f'Reprovado - Média:{media}')

# 14
lab = float(input('Nota do trabalho no laboratório: '))*2
semestral = float(input('Nota do trabalho semestral: '))*3
ex_final = float(input('Nota do exame final: ')) * 5

media = (lab+semestral+ex_final)/10

if media < 3:
    print(f'Reprovado. Média: {media}')
elif media < 5 and media >=3:
    print(f'Recuperação. Média: {media}')
else:
    print(f'Aprovado! Média: {media}')

# 15
dias = {1: 'Domingo', 2: 'Segunda-Feira', 3: 'Terça-Feira', 4: 'Quarta-Feira',
        5: 'Quinta-Feira', 6: 'Sexta-Feira', 7: 'Sábado'}

d = int(input('Infome o dia da semana:'))

if d < 1 or d > 7:
    print('Número invalido')
else:
    print(dias.get(d))

# 16
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
         7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

m = int(input('Informe o mês:'))

if m < 1 or m > 12:
    print('Número inválido')
else:
    print(meses.get(m))

# 17
bme = float(input('Informe a base menor do trapézio: '))
bma = float(input('Informe a base maior do trapézio: '))
a = float(input('Informe a altura do trapézio: '))

area = (bma+bme)*a/2

if bme <= 0 or bma <= 0:
    print('As bases devem ser maiores que 0')
else:
    print(f'A área do trapézio é: {area}')

operacao = input('Escolha a operação Adição (+), Subtração (-), Multiplicação (x) ou '
                 'Divisão (/):  ')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

# 18
if operacao == '+':
    print(f'Resultado: {n1+n2}')
elif operacao == '-':
    print(f'Resultado: {n1-n2}')
elif operacao == 'x':
    print(f'Resultado: {n1*n2}')
elif operacao == '/':
    print(f'Resultado: {n1/n2}')
else:
    print('Operação inválida')

# 19
n = int(input('Digite um número inteiro: '))
if n % 3 == 0 and n % 5 == 0:
    print('O número é divisivel por 3 e 5')
elif n % 3 == 0 and n % 5 != 0:
    print('O número é divisivel por 3 mas não por 5')
elif n % 5 == 0 and n % 3 != 0:
    print('O número é divisivel por 5 mas não por 3')
else:
    print('O número não é divisivel por 5 e nem por 3')

# 20
a = float(input('Infome o lado "A" do triângulo: '))
b = float(input('Infome o lado "B" do triângulo: '))
c = float(input('Infome o lado "C" do triângulo: '))

if a > b+c or b > a+c or c > a+b:
    print('Não é um triângulo')
elif a == b and b == c:
    print('Triâgulo equilátero')
elif a == b and a != c:
    print('Triângulo isósceles')
elif a == c and a != b:
    print('Triângulo isósceles')
elif c == b and c != a:
    print('Triâgulo isósceles')
else:
    print('Triângulo escaleno')

# 21
print('1 - Soma de 2 números \n'
      '2 - Diferença entre 2 números \n'
      '3 - Produto entre 2 números \n'
      '4 - Divisão entre 2 números (denominador não pode ser 0)')
opcao = int(input('Digite a opção: '))


if opcao == 1:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f'Resultado: {n1 + n2}')
elif opcao == 2:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if n1 > n2:
        print(f'Resultado: {n1 - n2}')
    else:
        print(f'Resultado: {n2 - n1}')
elif opcao == 3:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f'Resultado: {n1 * n2}')
elif opcao == 4:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if n2 == 0:
        print('O denominador não pode ser 0')
    else:
        print(f'Resultado: {n1 / n2}')
else:
    print('Opção inválida')

# 22
idade = int(input('Informe a idade: '))
tempo = int(input('Informe o tempo de serviço: '))

if idade >= 65:
    print('É possível se aposentar')
elif tempo >= 30:
    print('É possível se aposentar')
elif idade >= 60 and tempo >= 25:
    print('É possível se aposentar')
else:
    print('Não é possível se aposentar')

# 23
ano = int(input('Informe o ano: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 1:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

# 24
valor = float(input('Informe o valor do produto: R$'))
uf = (input('SP\n'
            'RJ\n'
            'MG\n'
            'MS\n'
            'Informe o estado: '))

if uf == 'SP' or uf == 'sp':
    print(f'Valor: R${(valor + (valor * 12) / 100):.2f}')
elif uf == 'RJ' or uf == 'rj':
    print(f'Valor: R${(valor + (valor * 15) / 100):.2f}')
elif uf == 'MG' or uf == 'mg':
    print(f'Valor: R${(valor + (valor * 7) / 100):.2f}')
elif uf == 'MS' or uf == 'ms':
    print(f'Valor: R${(valor + (valor * 8) / 100):.2f}')
else:
    print('UF inválida')

# 25

# 26
km = float(input('Informe a quantidade de km: '))
lt = float(input('Informe a quantidade de litros: '))

kmpl = km/lt

if kmpl < 8:
    print('Venda o carro!\n'
          f'{kmpl:.1f} litros por kilometro')
elif kmpl > 8 and kmpl <14:
    print('Econômico!\n'
          f'{kmpl:.1f} litros por kilometro')
elif kmpl > 12:
    print('Super econômico!\n'
          f'{kmpl:.1f} kilometros por litro')

# 27
idade = int(input('Informe a idade do nadador: '))
if idade >= 5 and idade <= 7:
    print('Infaltil A')
elif idade >= 8 and idade <= 10:
    print('Infaltil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Sênior')
else:
    print('Idade não aceita')

# 28
n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))

opcao = input('(a) - Geometrica\n'
              '(b) - Ponderada\n'
              '(c) - Harmônica\n'
              '(d) - Aritmética\n'
              'Qual média deseja fazer: ')

if opcao == 'A' or opcao == 'a':
    print(f'A média geométrica é {(n1*n2*n3)**(1/3)}')
elif opcao == 'B' or opcao == 'b':
    n2 = n2*2
    n3 = n3*3
    print(f'A média ponderada é {(n1+n2+n3)/6:.1f}')
elif opcao == 'C' or opcao == 'c':
    harmonica = 1 / (1 / n1) + (1 / n2) + (1 / n3)
    print(f'A média harmônica é {harmonica}')
elif opcao == 'D' or opcao == 'd':
    print(f'A média aritmética é {(n1+n2+n3)/3}')

# 29
from random import randrange
acertos = 0
i = 0
resultados = []
while i < 5:
    n1 = randrange(0, 100)
    n2 = randrange(0, 100)
    res = int(input(f'{n1} + {n2}\n'
                    f'Qual é a resposta?: '))
    i = i + 1
    resultado = n1 + n2
    resultados.append(str(f'{n1} + {n2} = {resultado}'))
    if res == resultado:
        acertos = acertos+1

for elemento in resultados:
    print(str(elemento))
print(f'Você acertou {acertos} perguntas')

# 30
lista = []
n1 = float(input('Digite o primeiro número:'))
lista.append(n1)
n2 = float(input('Digite o segundo número:'))
lista.append(n2)
n3 = float(input('Digite o terceiro número:'))
lista.append(n3)

lista.sort()
for n in lista:
    print(n)

# 31
altura = float(input('Infome sua altura: '))
peso = float(input('Informe seu peso: '))

if altura < 1.20 and peso <= 60:
    print('Categoria: A')
elif altura < 1.20 and peso > 60 and peso <= 90:
    print('Categoria D')
elif altura < 1.20 and peso > 90:
    print('Categoria G')
elif altura >= 1.20 and altura <= 1.70 and peso <= 60:
    print('Categoria B')
elif altura >= 1.20 and altura <= 1.70 and peso > 60 and peso <=90:
    print('Categoria C')
elif altura >= 1.20 and altura <= 1.70 and peso > 90:
    print('Categoria H')
elif altura > 1.70 and peso <= 60:
    print('Categoria C')
elif altura > 1.70 and peso > 60 and peso <=90:
    print('Categoria F')
elif altura > 1.70 and peso >90:
    print('Categoria I')
else:
    print('Não identificado')

# 32
produtos = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.00}

print('100 - Cachorro-Quente - R$1,20\n'
      '101 - Bauru Simples - R$1,30\n'
      '102 - Bauru com Ovo - R$1,50\n'
      '103 - Hambuguer - R$1,20\n'
      '104 - Cheeseburger - R$1,70\n'
      '105 - Suco - R$2,20\n'
      '106 - Refrigerante - R$1,00'
      )
opcao = int(input('Qual a opção: '))
qtd = int(input('Quantidade: '))

if opcao == 100:
    print(f'Valor: R${produtos.get(100)*qtd:.2f}')
elif opcao == 101:
    print(f'Valor: R${produtos.get(101)*qtd:.2f}')
elif opcao == 102:
    print(f'Valor: R${produtos.get(102) * qtd:.2f}')
elif opcao == 103:
    print(f'Valor: R${produtos.get(103) * qtd:.2f}')
elif opcao == 104:
    print(f'Valor: R${produtos.get(104) * qtd:.2f}')
elif opcao == 105:
    print(f'Valor: R${produtos.get(105) * qtd:.2f}')
elif opcao == 106:
    print(f'Valor: R${produtos.get(106)*qtd:.2f}')
else:
    print('Produto não identificado')

# 33
valor = float(input('Qual o valor do produto? R$'))
v_atual = 0

if valor <= 50:
    v_atual = valor + (5*valor)/100
elif valor > 50 and valor <= 100:
     v_atual = valor + (10*valor)/100
elif valor > 100:
    v_atual = valor + (15*valor)/100

print(f'O novo valor é R$:{v_atual:.2f}')
if v_atual <= 80:
    print('Barato')
elif v_atual > 80 and v_atual <= 120:
    print('Normal')
elif v_atual > 120 and v_atual <= 200:
    print('Caro')
else:
    print('Muito Caro')

# 34
nota = float(input('Informe a nota: '))
faltas = int(input('Informe a quantidade de faltas: '))

if nota >=9 and nota <=10 and faltas <= 20:
    print('Conceito: A')
elif nota >=9 and nota <=10 and faltas > 20:
    print('Conceito: B')
elif nota >=7.5 and nota <=8.9 and faltas <= 20:
    print('Conceito: B')
elif nota >=7.5 and nota <=8.9 and faltas > 20:
    print('Conceito: C')
elif nota >= 5.0 and nota <= 7.4 and faltas <= 20:
    print('Conceito: C')
elif nota >= 5.0 and nota <= 7.4 and faltas > 20:
    print('Conceito: D')
elif nota >= 4.0 and nota <= 4.9 and faltas <= 20:
    print('Conceito: D')
elif nota >= 4.0 and nota <= 4.9 and faltas > 20:
    print('Conceito E')
elif nota < 4.0 and nota >0:
    print('Conceito')
else:
    print('Nota não aceita')

# 35
l31 = [1, 3, 5, 7, 8, 10, 12]

dia = int(input('Informe o dia: '))
if dia < 0 or dia > 31:
    print('Dia inválido')
    exit()
else:
    mes = int(input('Informe o mês: '))
    if mes < 0 or mes > 12:
        print('Mês inválido')

    elif mes == 2 and dia > 29:
        print('Dia inválido para o mês de Fevereiro')
        exit()
    elif dia == 31 and mes not in l31:
        print('Esse mês não tem 31 dias')
        exit()
    else:
        ano = int(input('Informe o ano: '))

bissexto = True
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 1:
    bissexto = True
else:
    bissexto = False

if mes == 2 and dia == 29 and bissexto == True:
    print(f'Data válida: {dia}/{mes}/{ano}')
elif mes == 2 and dia == 29 and bissexto == False:
    print(f'Dia 29 não aceito no mês de fevereiro pois o ano não é bissexto')
else:
    print(f'Data válida: {dia}/{mes}/{ano}')

# 36
venda = float(input('Informe o valor de vendas: R$'))

if venda < 20000:
    print(f'Comissão: R${400 + (venda * 14) / 100:.2f}')
elif venda < 40000 and venda >= 20000:
    print(f'Comissão: R${500 + (venda * 14) / 100:.2f}')
elif venda < 60000 and venda >= 40000:
    print(f'Comissão: R${550 + (venda * 14) / 100:.2f}')
elif venda < 80000 and venda >= 60000:
    print(f'Comissão: R${600 + (venda * 14) / 100:.2f}')
elif venda < 100000 and venda >= 80000:
    print(f'Comissão: R${650 + (venda * 14) / 100:.2f}')
else:
    print(f'Comissão: R${700 + (venda * 16) / 100:.2f}')

# 37
chegada = list(map(int,
                   input('Insira o momento de chegada (ex: 12 50): ').split()))

while (chegada[0]) * (chegada[0] - 23) > 0 or (chegada[1]) * (chegada[1] - 59) > 0:
    print('Horário inválido!')
    chegada = list(map(int,
                       input('Insira o momento de chegada (ex: 12 50): ').split()))

saida = list(map(int, input('Insira o momento de saída (ex: 13 10): ').split()))

while (saida[0]) * (saida[0] - 23) > 0 or (saida[1]) * (saida[1] - 59) > 0:
    print('Horário inválido!')
    saida = list(map(int,
                     input('Insira o momento de saída (ex: 13 10): ').split()))

hora_chegada = chegada[0] + chegada[1] / 60
hora_saida = saida[0] + saida[1] / 60
tempo_total = hora_saida - hora_chegada

if hora_chegada >= hora_saida:
    tempo_total = (24 - hora_chegada) + hora_saida

if int(tempo_total) < tempo_total:
    tempo_total = int(tempo_total) + 1
else:
    tempo_total = int(tempo_total)

custo_total = 0.0
if tempo_total <= 2:
    custo_total = tempo_total * 1
elif tempo_total <= 4:
    custo_total = 2 + (tempo_total - 2) * 1.4
else:
    custo_total = 4.8 + (tempo_total - 4) * 2

print(f'O custo total do estacionamento é de R$ {custo_total:.2f}')

# 38
l31 = [1, 3, 5, 7, 8, 10, 12]

dia = int(input('Informe o dia: '))
if dia < 0 or dia > 31:
    print('Dia inválido')
    exit()
else:
    mes = int(input('Informe o mês: '))
    if mes < 0 or mes > 12:
        print('Mês inválido')
        exit()
    elif mes == 2 and dia > 29:
        print('Dia inválido para o mês de Fevereiro')
        exit()
    elif dia == 31 and mes not in l31:
        print('Esse mês não tem 31 dias')
        exit()
    else:
        ano = int(input('Informe o ano: '))
        if ano > 2020:
            print('Ano inválido')
            exit()

bissexto = True
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 1:
    bissexto = True
else:
    bissexto = False

if mes == 2 and dia == 29 and bissexto == True:
    print(f'Data válida: {dia}/{mes}/{ano}')
elif mes == 2 and dia == 29 and bissexto == False:
    print(f'Dia 29 não aceito no mês de fevereiro pois o ano não é bissexto')
else:
    print(f'Data Nascimento: {dia}/{mes}/{ano}')

# 39
salario = float(input('Informe o salário atual: R$'))
tempo = int(input('Informe o tempo de serviço em anos: '))

if salario <= 500:
    salario = salario + (salario * 25) / 100
elif salario > 500 and salario <= 1000:
    salario = salario + (salario * 20) / 100
elif salario > 1000 and salario <= 1500:
    salario = salario + (salario * 15) / 100
elif salario > 1500 and salario <= 2000:
    salario = salario + (salario * 10) / 100
else:
    salario = salario

if tempo < 1:
    salario = salario
elif tempo >= 1 and tempo <= 3:
    salario = salario + 100
elif tempo >=4 and tempo <= 6:
    salario = salario + 200
elif tempo >=7 and tempo <= 10:
    salario = salario + 300
else:
    salario = salario + 500

print(f'R${salario:.2f}')

# 40
custo = float(input('Informe o valor do Custo de Fábrica: R$'))

if custo <= 12000:
    custo = custo + (custo * 5) / 100
elif custo > 12000 and custo <= 25000:
    custo = custo + (custo * 10) / 100 + (custo * 15) / 100
else:
    custo = custo + (custo * 15) / 100 + (custo * 20) / 100

print(f'O custo final é R${custo:.2f}')

# 41
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura*altura)

if imc <= 18.5:
    print(f'IMC: {imc:.1f} - Abaixo do peso')
elif imc > 18.5 and imc <= 24.9:
    print(f'IMC: {imc:.1f} - Peso Saudável')
elif imc > 24.9 and imc <=29.9:
    print(f'IMC: {imc:1.f} - Peso em excesso')
elif imc > 29.9 and imc <= 34.9:
    print(f'IMC: {imc:.1f} - Obesidade Grau I')
elif imc > 34.9 and imc < 39.9:
    print(f'IMC: {imc:.1f} - Obesidade Grau II (severa)')
else:
    print(f'IMC: {imc:.1f} - Obesidade Grau III (mórbida)')
"""











