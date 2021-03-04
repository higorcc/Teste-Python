# Exercicios modulo 4 - Váriaveis e tipos de dados
"""
# 1
n = int(input('Digite um número inteiro: '))
print(n)

# 2
n = float(input('Digite um número real: '))
print(n)

# 3
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

res = n1+n2+n3
print(res)

# 4
n = float(input('Digite um número para calcular a raiz quadrada: '))
res = n*n
print(res)

# 5
n = float(input('Digite um número para calcular a quinta parte dele: '))
res = n/5
print(res)

# 6
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = celsius*(9.0/5.0)+32.0
print("%.2f" % fahrenheit)

# 7
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
celsius = 5.0*(fahrenheit-32.0)/9.0
print("%.2f" % celsius)

# 8
kelvin = float(input('Digite a temperatura em graus Kelvin: '))
celsius = kelvin - 273.15
print("%.2f" % celsius)

# 9
celsius = float(input('Digite a temperatura em graus Celsius: '))
kelvin = celsius + 273.15
print("%.2f" % kelvin)

# 10
km_h = float(input('Digite os km/h: '))
m_s = km_h/3.6
print("%.4f" % m_s)

# 11
m_s = float(input('Digite os metros por segundo: '))
km_h = m_s*3.6
print("%.1f" % km_h)

# 12
milhas = float(input('Digite uma distância em milhas: '))
km = 1.61 * milhas
print("%.5f" % km)

# 13
km = float(input('Digite uma distância em km: '))
milhas = km/1.61
print("%.5f" % milhas)

# 14
graus = float(input('Digite um ângulo em graus:'))
radiano = graus*3.14/180
print(radiano)

# 15
radiano = float(input('Digite um ângulo em radiano:'))
graus = radiano*180/3.14
print(graus)

# 16
polegadas = float(input('Digite um valor em polegadas: '))
centimetros = polegadas*2.54
print(centimetros)

# 17
centimetros = float(input('Digite um valor em centimetros: '))
polegadas = centimetros/2.54
print("%.4f" % polegadas)

#18
m3 = float(input('Digite um valor em metros cubicos: '))
litros = 1000*m3
print(litros)

# 19
litros = float(input('Digite um valor em litros: '))
m3 = litros/1000
print(m3)

# 20
kg = float(input('Digite um valor em kilos: '))
libras = kg/0.45
print(libras)

# 21
libras = float(input('Digite um valor em libras: '))
kg = libras*0.45
print(kg)

# 22
jardas = float(input('Digite um valor em jardas: '))
metros = 0.91*jardas
print(metros)

# 23
metros = float(input('Digite um valor em metros: '))
jardas = metros/0.91
print(jardas)

# 24
m2 = float(input('Digite um valor em metros quadrados: '))
acres = m2*0.000247
print(acres)

# 25
acres = float(input('Digite um valor em acres: '))
m2 = acres*4048.58
print(m2)

# 26
m2 = float(input('Digite um valor em metros quadrados: '))
hectares = m2*0.0001
print(hectares)

# 27
hectares = float(input('Digite um valor em hectares: '))
m2 = hectares*10000
print(m2)

# 28
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digigte o segundo valor: '))
n3 = float(input('Digigte o terceiro valor: '))

res = (n1*n1)+(n2*n2)+(n3*n3)
print(res)

# 29
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1+nota2+nota3+nota4)/4
print("%.1f" % media)

# 30
real = float(input('Digite o valor em Real R$'))
dolar = real*0.19
print(f'R${real} são US${dolar}')

# 30.2
dolar = float(input('Digite o valor em Dolar US$'))
real = dolar*5.28
print(f'US${dolar} são R${real}')

# 31
n = int(input('Informe um número: '))
print(f'Antecessor: {n-1}\n'
      f'Sucessor: {n+1}')

# 32
n = int(input('Informe um número: '))
st = (n*3)+1
ad = (n*2)-1
res = st+ad
print(res)

# 33
quadrado = float(input('Informe a base ou altura do quadrado: '))
area = quadrado*quadrado
print(area)


# 34
raio = float(input('Informe o raio do circulo: '))
area = 3.141592*(raio*raio)
print(area)

# 35
import math
cateto1 = float(input('Informe a medida do primeiro cateto: '))
cateto2 = float(input('Informe a medida do segundo cateto: '))
res = (cateto1*cateto1)+(cateto2*cateto2)
hipotenusa = math.sqrt(res)
print("%.2f" % hipotenusa)

# 36
altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro:'))
volume = 3.141592*(raio*raio)*altura
print(volume)

# 37
valor = float(input('Digite o valor do produto: R$'))
valor_desconto = (12*valor)/100
print(f'O valor final é de {valor-valor_desconto}\n'
      f'O desconto foi de {valor_desconto}')

# 38
salario = float(input('Informe o valor do salário: R$'))
aumento = (25*salario)/100
print(f'O salário é R${salario+aumento}\n'
      f'O aumento foi de R${aumento}')

# 39
importancia = 780000.00
pganhador = (46*importancia)/100
sganhador = (32*importancia)/100
tganhador = (22*importancia)/100
print(f'O primeiro ganhador ficou com R${pganhador}\n'
      f'O segundo com R${sganhador}\n'
      f'O terceiro com R${tganhador}')

# 40
qtd_dias = int(input('Quantos dias foram trabalhados:'))
valor_bruto = 30*qtd_dias
desconto = (8*valor_bruto)/100
print(f'Dias trabalhados: {qtd_dias}\n'
      f'Valor à receber: R${valor_bruto-desconto}\n'
      f'Valor do desconto IR: R${desconto}')

# 41
valor_hora = float(input('Informe o valor da hora trabalhada: R$'))
horas_trabalhadas = int(input('Informe as horas trabalhas/mês: '))
valor1 = valor_hora*horas_trabalhadas
acrescimo = (valor1*10)/100
valor_total = valor1+acrescimo
print(f'Valor a receber: R${"%.2f" % valor_total}\n'
      f'Acréscimo de: R${"%.2f" % acrescimo}')

# 42
salario_base = float(input('Informe o salário base: R$'))
gratificacao = (salario_base*5)/100
imposto = (salario_base*7)/100
total = (salario_base+gratificacao)-imposto
print(f'Valor a receber: R${total}\n'
      f'Gratificacao: R${gratificacao}\n'
      f'Imposto pago: R${imposto}')

# 43
venda = float(input('Qual o valor da venda: R$'))
tipo_venda = input('Informe o tipo da compra P - (Parcelado) - V - (A vista): ')
desconto = (10 * venda) / 100
valor_final = venda-desconto
parcela = (venda - desconto) / 3
comissao_vendedor = float(0)
if tipo_venda == 'V':
    comissao_vendedor = (5 * (venda - desconto) / 100)
else:
    comissao_vendedor = (5 * venda) / 100
    print(f'Valor da parcela (3): R${"%.2f" % parcela}')

print(f'Valor total com desconto R${"%.2f" % valor_final}\n'
      f'Comissão do vendedor: {"%.2f" % comissao_vendedor}'
      )

# 44
a = float(input('Qual é a altura do degrau da escada (cm)? '))
ab = float(input('Qual é a altura que você deseja alcançar subindo a escada (metros)? '))
x = ab / a

print(f'O usuário deverá subir {x} degraus para alcançar o objetivo.')

# 45
frase = input('Digite uma letra ou frase em maiusculo: ')
print(f'Conversão: {frase.lower()}')

# 46
n = int(input('Digite um valor inteiro de 100 à 999: '))
conversao_string = str(n)
inversao = conversao_string[::-1]
conversao_num = int(inversao)
print(f'Número invertido: {conversao_num}')
print(type(conversao_num))

# 47
numero = int(input('Informe um número entre 1000 e 9999: '))
if numero >= 1000 and numero <= 9999:
    for n in str(numero):
        print(n)

# 48
segundos = int(input('Informe o valor em segundos: '))
print(f'Minutos: {segundos/60}')
print(f'Horas: {segundos/3600}')
print(f'Segundos: {segundos}')

# 49
import datetime as dt

inicio = dt.datetime.now()
duracao = int(input('Informe a quantidade de duração em segundos: '))
fim = inicio + dt.timedelta(seconds=duracao)
print(f'Inicio: {inicio}')
print(f'Fim:    {fim}')

# 50
idade = int(input('Qual a sua idade? '))
pergunta = input('Já fez aniversário esse ano? ')
ano_atual = 2021
nascimento = 0
if pergunta == 'Sim':
    nascimento = ano_atual-idade
    print(f'Você nasceu em {nascimento}')
elif pergunta == 'Não':
    nascimento = (ano_atual-idade)-1
    print(f'Você nasceu em {nascimento}')
else:
    print('Resposta invalida')

# 51
x1 = 0
y1 = 0
x2 = int(input('Digite o valor do ponto x2:'))
y2 = int(input('Digite o valor do ponto y2:'))

formula = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(f'A distância da origem é: {formula:.2f}')


# 52

# 53
# 53
c = float(input('Qual é o comprimento do terreno? '))
l = float(input('Qual é a largura do terreno? '))
p = float(input('Qual é o preço do metro de tela p? '))
pc = p * c * l

print(f'O custo para cercar este mesmo terreno com tela é de R${pc:.2f}')
"""






