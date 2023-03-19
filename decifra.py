#2464 - Decifra

alfabeto = list('abcdefghijklmnopqrstuvwxyz')
sequencia = list(input())
mensagem = input()
decifrado = ''
for l in mensagem:
    indexletra = sequencia.index(l)
    decifrado += alfabeto[indexletra]
print(decifrado)
