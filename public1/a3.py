#Controle de estoque - Simples
ctg = input('Categoria disponíveis:\n\n[1]Alimentos \n[2]Bebidas \n[3]Limpeza \n\nQual você deseja? ')
while ctg.isalpha() or ctg == '':
    print('\nDigite um valor válido!\n')
    if int(ctg) == 0 or int(ctg) > 3:
        print('\nDigite um valor válido!\n')
    ctg = input('Categoria disponíveis:\n[1]Alimentos \n[2]Bebidas \n[3]Limpeza \nQual categoria você deseja? ')

prod = str(input('Nome do produto: ')).capitalize()
while prod == '':
    print('\nDigite um valor válido!\n')
    prod = str(input('Nome do produto: ')).capitalize()

qtd = input('Quantidade em estoque: ')
while qtd.isalpha() or qtd == '':
    print('\nDigite um valor válido!\n')
    qtd = input('Quantidade em estoque: ')

alimentos = 50
bebidas = 75
limpeza = 30

if int(ctg) == 1 and int(qtd) < alimentos:
    print(f'\nSolicitar {prod} à equipe de compras, temos apenas {qtd} em estoque')
elif int(ctg) == 2 and int(qtd) < bebidas:
    print(f'\nSolicitar {prod} à equipe de compras, temos apenas {qtd} em estoque')
elif int(ctg) == 3 and int(qtd) < limpeza:
    print(f'\nSolicitar {prod} à equipe de compras, temos apenas {qtd} em estoque')
else:
    print('\nEstoque completo')