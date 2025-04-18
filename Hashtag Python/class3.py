produtos = ['computador','livro','tablet','celular','tv','ar condicionado','alexa','máquina de café','kingle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem:

produtos_ecommerce = [[10000,2500],[5000,40],[7000,1200],[20000,1500],[5800,1300],[7200,2500],[200,800],[3300,700],[1900,400]]

if 'livro' in produtos:
    i_prod = produtos.index('livro')
    print(i_prod)
    print(produtos_ecommerce[i_prod][1])
    produtos_ecommerce[i_prod][1] += produtos_ecommerce[i_prod][1] * 10 / 100
    print(produtos_ecommerce[i_prod])