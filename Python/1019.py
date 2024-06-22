tempo = int(input())
unidades = [3600, 60, 1]
horario = []
for i in unidades:
    horario.append(tempo // i)
    tempo %= i
horas, minutos, segundos = horario
print(f'{horas}:{minutos}:{segundos}')