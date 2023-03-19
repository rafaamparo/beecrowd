#2449 - Fechadura

num, senha = map(int, input().split())
mov = 0
dif = 0
alturas =  list(map(int, input().split()))
while alturas.count(senha) != num:
    for i in range (len(alturas) - 1):
        dif = senha - int(alturas[i])
        mov += abs(dif)
        alturas[i] += dif
        alturas[i+1] += dif
print(mov)
