"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída


# Diferença entre parâmetros e argumentos:
- Parâmetros são variáveis declaradas na definição de uma função
- Argumentos são dados passados durante a execução de uma função

A ordem dos argumentos importam, a não ser que utilize Argumentos Nomeados
"""


# Refatorando uma função
def calcular_quadrado(numero):
    return numero * numero


print(calcular_quadrado(3))


# Refatorando outra função...
# As funções podem ter N parâmetros de entrada, são separados por virgulas
def cantar_parabens(aniversariante, qtd):
    for i in range(qtd):
        print('Parabéns pra você')
        print('Nessa data querida')
        print('Muitas felicidades')
        print('Muitos anos de vida')
        print(f'Viva o {aniversariante}')
        print('-' * 10)


cantar_parabens('Higor', 3)


# Função com strings como parâmetro
def nome(nome, sobrenome):
    print(f'O nome completo é: {nome} {sobrenome}')


nome('Breno', 'Lopes')


# Argumentos Nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos, podemos utilizar qualquer ordem
nome(sobrenome='Lopes', nome='Breno')
