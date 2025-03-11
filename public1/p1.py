from random import randint



print(f'Os valores sorteados foram:', end = ' ')

sort = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))

for kdns in range(0,5):
    print(f'{kdns}', end = ' ~ ')
print(f'\nO maior valor foi: {max(sort)}')
print(f'O menor valor foi {min(sort)}')