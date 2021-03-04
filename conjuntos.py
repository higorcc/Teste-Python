"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;
"""

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7})    # Contém números repetidos
print(s)
print(type(s))

# Forma 2  - Mais comum
s = {1, 2, 3, 4, 5, 5, 6}
print(s)


# Importante lembrar que além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista= {lista} com {(len(lista))} elementos')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla= {tupla} com {(len(tupla))} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario= {dicionario} com {(len(dicionario))} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto= {conjunto} com {(len(conjunto))} elementos')


# Iterar sobre um conjunto(set)

for numero in conjunto:
    print(numero)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

cidade_unica = set(cidades)
print(cidade_unica)

# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)

s.add(4)
print(s)


# Remover elementos do conjunto
# Forma 1 -  Obs: Se o elemento não for encontrado, retornará um erro

s.remove(3)      # Não é indice! Informamos o valor a ser removido.
print(s)

# Forma 2 -  Obs: Se o elemento não for encontrado, nada ocorre

s.discard(2)
print(s)


# Copiando um conjunto para outro

# Forma 1 -  Deep Copy

novo = s.copy()
print(novo)

novo.add(2)

print(f'Depois da alteração {s}')
print(f'Depois da alteração {novo}')


# Forma 2 - Shallow copy

novo = s

novo.add(5)

print(f'Depois da alteração {s}')
print(f'Depois da alteração {novo}')


# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

####

# Temos dois conjuntos: Um contendo alunos do curso de Python e o outro de Java

estudantes_python = {'Higor', 'Pedro', 'Alex', 'Maria', 'Patricia', 'Milton'}
estudantes_java = {'Gabriel', 'Allan', 'Alex', 'Victor', 'Maria'}

# Alguns alunos do curso de Java também cursam Python

# Gerar um conjunto com nomes de alunos únicos
# Forma 1 - Utilizando Union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere Pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)


# Gerar uma lista de alunos que estão em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar uma lista de estudantes que não estão em ambos
so_python = estudantes_python.difference(estudantes_java)
print(f'Estudantes somente de Python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f'Estudantes somente de Java: {so_java}')


# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
