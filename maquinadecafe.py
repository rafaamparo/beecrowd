#2670 - Máquina de Café

a1 = int(input())
a2 = int(input())
a3 = int(input())
t1 = a2*2 + a3*4
t2 = 2*(a1+a3)
t3 = a2*2 + a1*4
if t1 <= t2:
    menor = t1
else:
    menor = t2
if menor >= t3:
    menor = t3
print(menor)
