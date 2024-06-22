import math
pontos = []
for _ in range(2):
    ponto = list(map(float, input().split()))
    pontos.extend(ponto)
x1, y1, x2, y2 = pontos
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'{distancia:.4f}')