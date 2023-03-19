#2301 - Vivo ou Morto

part, rodadas = map(int, input().split())
teste = 1

while part != 0 and rodadas != 0:
    fila = input().split()
    for _ in range(rodadas):
        n, ordem, *acao = map(int, input().split())
        for j in range(n-1, -1, -1):
            if acao[j] != ordem:
                fila.pop(j)
    print('Teste', teste)
    print(fila[0])
    print()
    teste += 1
    part, rodadas = map(int, input().split())
