tempo, velocidade = map(int, (input() for _ in range(2)))
combustivel = velocidade * tempo / 12
print(f'{combustivel:.3f}')