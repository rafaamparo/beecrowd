# problema 1397 - Jogo do Maior

num_partidas = int(input())
while num_partidas != 0:
    pontos_a = 0
    pontos_b = 0
    for i in range (num_partidas):
        jogadas = input().split()
        if int(jogadas[0]) > int(jogadas[1]):
            pontos_a +=1
        elif int(jogadas[1]) > int(jogadas[0]):
            pontos_b +=1
    print(pontos_a, pontos_b)
    num_partidas = int(input())
