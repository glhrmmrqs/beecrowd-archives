nome_vendedor = str(input())
salario_fixo, total_vendas = map(float, (input() for _ in range(2)))
salario_total = salario_fixo + total_vendas * 0.15
print(f'TOTAL = R$ {salario_total:.2f}')