meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas_1sem = [25000,29000,22200,17750,15870,19900]
vendas_2sem = [19850,20120,17540,15555,49051,9650]
vendas_anual = vendas_1sem + vendas_2sem
i_max = vendas_anual.index(max(vendas_anual))
i_min = vendas_anual.index(min(vendas_anual))
print(f'\nO melhor mês do ano foi {meses[i_max].capitalize()} com {max(vendas_anual)} vendas')
print(f'O pior mês do ano foi {meses[i_min].capitalize()} com {min(vendas_anual)} vendas')
print(f'O faturamento total foi de {sum(vendas_anual):,.2f}')
print(f'O melhor mês representou {max(vendas_anual)/sum(vendas_anual):.1%}')


print('\n\nOS 3 MELHORES VALORES DO ANO\n')
print(f'1ª valor = {max(vendas_anual):,.2f}')
lst_top3 = []
lst_top3.append(max(vendas_anual))
vendas_anual.remove(max(vendas_anual))

print(f'2ª valor = {max(vendas_anual):,.2f}')
lst_top3.append(max(vendas_anual))
vendas_anual.remove(max(vendas_anual))

print(f'2ª valor = {max(vendas_anual):,.2f}')
lst_top3.append(max(vendas_anual))

