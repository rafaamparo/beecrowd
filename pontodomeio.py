#3056 - Ponto do Meio

n = int(input())
lado = 2
for _ in range(n):
    lado += (lado-1)

pontos = lado**2
print(pontos)
