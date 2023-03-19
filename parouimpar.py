#problema 2286 - Par ou Ímpar

n = int(input())
t = 1
while n != 0:
    print ('Teste', t)
    nome1 = input()
    nome2 = input()
    for i in range(n):
        numeros = input().split()
        if  (int(numeros[0]) + int(numeros [1])) % 2 == 0:
            print (nome1)
        else:
            print (nome2)
    print('')
    t += 1
    n = int(input())
