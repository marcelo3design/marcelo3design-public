produtos = ['computador','livro','tablet','celular','tv','ar condicionado','alexa','máquina de café','kingle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem:

produtos_ecommerce = [[10000,2500],[50000,40],[7000,1200],[20000,1500],[5800,1300],[7200,2500],[200,800],[3300,700],[1900,400]]

if 'livro' in produtos:
    i_prod = produtos.index('livro')

    print(f'O valor de cada livro sem tributo é {produtos_ecommerce[i_prod][1]}')
    print(f'Para {produtos_ecommerce[i_prod][0]} livros, o custo saíria de {produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]:,.2f}\n')
    preco_normal = produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]




    produtos_ecommerce[i_prod][1] += produtos_ecommerce[i_prod][1] * 10 / 100
    print(f'Agora, o valor de cada livro com tributo é {produtos_ecommerce[i_prod][1]:.0f}')
    preco_aumento = produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]

    aumento = preco_aumento - preco_normal
    print(f'O valor de {produtos_ecommerce[i_prod][0]} é de {produtos_ecommerce[i_prod][0] * produtos_ecommerce[i_prod][1]:,.2f} que equivale a um aumento de {(aumento / preco_normal) * 100 :.0f}%')


