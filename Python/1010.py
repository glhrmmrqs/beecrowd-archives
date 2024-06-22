total = 0
for _ in range(2):
    codigo, quantidade, valor = map(float, input().split())
    total += quantidade * valor
print(f'VALOR A PAGAR: R$ {total:.2f}')