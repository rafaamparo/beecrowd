#3058 - Supermercado

n = int(input())
precos = []
resultado = 0
for i in range(n):
    pg = list(map(eval, input().split()))
    ig = pg[0]/pg[1]
    precos.append(ig)
list.sort(precos)
resultado = precos[0] * 1000
print('{:.2f}'.format(resultado))
