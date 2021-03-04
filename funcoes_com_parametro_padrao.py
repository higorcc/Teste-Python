"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

"""


def exponencial(num=1, potencia=1):
    return num ** potencia


# Todos seriam validos
print(exponencial(8, 2))
print(exponencial(3))
print(exponencial())


# Utilizando uma váriavel global dentro do escopo da função

total = 0


def incrementa():
    global total        # Informando que é uma váriavel global
    total += 1
    return total


print('-' * 10)
print(incrementa())
print(incrementa())
