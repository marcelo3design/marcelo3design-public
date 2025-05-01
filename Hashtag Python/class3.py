produtos = ['computador','livro','tablet','celular','tv','ar condicionado','alexa','máquina de café','kingle']
produtos_ecommerce = [[10000,2500],[50000,40],[7000,1200],[20000,1500],[5800,1300],[7200,2500],[200,800],[3300,700],[1900,400]]
if 'livro' in produtos:
    print(f'\n\033[01;35m{'CUSTOS SEM IMPOSTOS':>30}\033[m\n')
    i_prod = produtos.index('livro')
    print(f'O valor de cada livro sem tributo é {produtos_ecommerce[i_prod][1]}')
    print(f'Para {produtos_ecommerce[i_prod][0]} livros, o custo saíria de {produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]:,.2f}\n')
    preco_normal = produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]
    produtos_ecommerce[i_prod][1] += produtos_ecommerce[i_prod][1] * 10 / 100
    print(f'\n\033[01;35m{'CUSTOS COM IMPOSTOS':>30}\033[m\n')
    print(f'Agora, o valor de cada livro com tributo é {produtos_ecommerce[i_prod][1]:.0f}')
    preco_aumento = produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]
    aumento = preco_aumento - preco_normal
    print(f'O valor de {produtos_ecommerce[i_prod][0]} é de {produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]:,.2f} que equivale a um aumento de {(aumento / preco_normal) * 100 :.0f}%')
    print('\n')
print(f'\n{'\033[01;35mQUANTIDADE PARA ALINHAR ESTOQUE':>45}\033[m\n')
for enum, kdv in enumerate(produtos_ecommerce):
    if produtos_ecommerce[enum][1] < 1000:
        print(f'\033[03;31;31m{produtos[enum].capitalize():<20}\033[m estoque a baixo do normal, adicione {1000 - produtos_ecommerce[enum][1]:.0f} para completar.')

