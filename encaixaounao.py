#1241 - Encaixa ou Não II

n = int(input())
if n != 0:
    for i in range(n):
        valores = input().split()
        if ((int(valores[0]) % 10**(len(valores[1])))) == int(valores[1]):
            print('encaixa')
        else: 
            print('nao encaixa')
