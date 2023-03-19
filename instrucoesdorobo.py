#1574 - Instruções do Robô

t = int(input())
for i in range(t):
    p = 0
    numinstruçoes = int(input())
    listamov = []
    for j in range(numinstruçoes):
        ordem = input().upper()
        if ordem == 'LEFT':
            p -= 1
            listamov.append(-1)
        elif ordem == 'RIGHT':
            p += 1
            listamov.append(1)
        else:
            acao = ordem.split()
            p += listamov[int(acao[2])-1]
            listamov.append(listamov[int(acao[2])-1])
    print(p)
