#problema 2247 - Cofinhos da Vó Vitória

depositos = int(input())
teste = 0
while depositos != 0:
    diferença = 0
    teste += 1
    print ('Teste', teste)
    for i in range (depositos):
        valores = input().split()
        diferença += int(valores[0]) - int(valores[1])
        print (diferença)
    print ('')
    depositos = int(input())
