quarto = list()
nome_cpf = list()
while True:
    nome_cpf.clear()
    nome_cpf.append(str(input('Digite o nome do cliente: ')).capitalize())
    nome_cpf.append(int(input('Digite o CPF do cliente: ')))
    quarto.append(nome_cpf[:])
    for kdv in quarto:
        print(kdv)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
