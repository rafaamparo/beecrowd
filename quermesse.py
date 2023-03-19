#problema 2189 - Quermesse

n = int(input())
vencedor = 0
teste = 0
ingressos = []
while n != 0:
    teste += 1
    print('Teste', teste)
    ingressos = input().split()
    for i in range (n):
        if int(ingressos[i]) == i+1:
            vencedor = ingressos[i]
    print(vencedor)
    print('')
    n = int(input())
    if n == 0:
        break
