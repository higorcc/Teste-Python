""""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada
"""
# Exemplo 1

for n in range(1, 11):
    if n == 6:
        break
    else:
        print(n)
print('Sai do loop')


# Exemplo 2

while True:
    comando = input('Digite "sair" para sair ')
    if comando == 'sair':
        break
