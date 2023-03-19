#problema 1467 - Zerinho ou Um
while True:
    try:
        jogadas = input().split()
        if jogadas[0] == jogadas[1] == jogadas[2]:
            print('*')
        elif jogadas[0] != jogadas[1] and jogadas[0] != jogadas[2] and jogadas[1] == jogadas[2]:
            print ('A')
        elif jogadas[1] != jogadas[0] and jogadas[1] != jogadas[2] and jogadas[0] == jogadas[2]:
            print ('B')
        else:
            print('C')
    except (EOFError):
        break
