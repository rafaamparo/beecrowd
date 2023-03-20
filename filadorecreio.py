#1548 - Fila do Recreio

n = int(input())
for _ in range(n):
    m = int(input())
    p = list(map(int, input().split()))
    lista_ordenada = sorted(p, reverse = True)
    cont = 0
    for j in range(len(lista_ordenada)):
        if p[j] == lista_ordenada[j]:
            cont += 1
    print(cont)
