# Exercício

carrinho = []
produto = ''

while produto != 'sair':
    produto = input('Adicione um produto ou digite sair: ')
    if produto != 'sair' and len(carrinho) < 10:
        carrinho.append(produto)
    elif produto == 'sair' and len(carrinho) == 0:
        print('Você não adicionou produtos ao carrinho')
    elif produto == 'sair':
        print('Os produtos adicionados ao carrinho são:')
        for chave, produto in enumerate(carrinho):
            print(chave + 1, ' - ', produto.title())
        break
    elif len(carrinho) == 10:
        print('Você atingiu a quantidade maxima de volumes \n'
              'Os produtos adicionados ao carrinho são:')
        for chave, produto in enumerate(carrinho):
            print(chave+1, ' - ', produto.title())
        break


print('-------------- Obrigado! --------------')
