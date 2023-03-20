#2782 - Escadinha

n = int(input())
sequencia = list(map(int, input().split()))
result = 0
maior = 10**6
menor = -(10**6)
if (len(sequencia)) == 1:
    print('1')
else:
    for i in range(len(sequencia)-1):
        if sequencia[i] - sequencia[i+1] != sequencia[i-1] - sequencia[i]:
            result += 1
    if result > maior:
        result = maior
    elif result < menor:
        result = menor
    print(result)
