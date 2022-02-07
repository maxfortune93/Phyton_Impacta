preco = float(input())              
qtd = int(input())             
preco_sem_desconto = preco * qtd
desconto_fixo = preco_sem_desconto * 0.1
desconto_unidade = preco_sem_desconto * (0.01 * qtd)
preco_final = preco_sem_desconto -(desconto_fixo + desconto_unidade)
print(f'{preco_sem_desconto:.2f}')
print(f'{preco_final:.2f}')
