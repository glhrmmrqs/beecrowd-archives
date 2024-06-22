numero_funcionario = int(input())
horas_trabalhadas, valor_hora = map(float, (input() for _ in range(2)))
salario = horas_trabalhadas * valor_hora
print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salario:.2f}')