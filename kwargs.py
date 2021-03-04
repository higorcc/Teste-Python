"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros detault (não obrigatórios);
- **kwargs

"""


# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(joao='verde', maria='preto', pedro='azul', carina='amarelo')


# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs.get('geek') == 'Python':
        return 'Você recebeu um cumprimento Pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs.get('geek')} Geek"
    return 'Não sei quem é você...'


print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Salve'))
print(cumprimento_especial(juao='Python'))


# Desempacotar com kwargs
def mostra_nome(**kwargs):
    return f"{kwargs['nome'], kwargs['sobrenome']}"


dicionario = {'nome': 'Higor', 'sobrenome': 'Campos'}
print(mostra_nome(**dicionario))





