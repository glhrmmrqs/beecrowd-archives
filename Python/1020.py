idade = int(input())
unidades = [365, 30, 1]
tempo = []
for i in unidades:
    tempo.append(idade // i)
    idade %= i
anos, meses, dias = tempo
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')