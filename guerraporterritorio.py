#2420 - Guerra por Território

n_seçoes = int(input())
comprimentos = list(map(int, input().split()))
tammedio = 0
divisao = 0
for c in comprimentos:
    tammedio += c
tammedio = (tammedio/2)
for i in range (len(comprimentos)-1):
    divisao += comprimentos[i]
    if divisao == tammedio:
        print(i+1)
        break
