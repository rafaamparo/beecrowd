#3059 - Pares de Números

n, min, max = map(int, input().split())
vetor = list(map(int, input().split()))
cont = 0
while len(vetor) > 0:
    for j in range(1, len(vetor)):
        if vetor[0] + vetor[j] >= min and vetor[0] + vetor[j] <= max:
            cont += 1
    vetor.pop(0)
print(cont)
