#2312 - Quadro de Medalhas

from functools import cmp_to_key
def cmp_medalhas(p1,p2):
    if int(p1[1]) > int(p2[1]):
        return -1
    elif int(p1[1]) < int(p2[1]):
        return 1
    elif int(p1[1]) == int(p2[1]):
        if int(p1[2]) > int(p2[2]):
            return -1
        elif int(p1[2]) < int(p2[2]):
            return 1
        elif int(p1[2]) == int(p2[2]):
            if int(p1[3]) > int(p2[3]):
                return -1
            elif int(p1[3]) < int(p2[3]):
                return 1
            elif int(p1[3]) == int(p2[3]):
                if p1[0] < p2[0]:
                    return -1
                elif p1[0] > p2[0]:
                    return 1
                else:
                    return 1

n = int(input())
lista = []
for _ in range(n):
    nome, o, p, b = input().split()
    dado = (nome, int(o), int(p), int(b))
    lista.append(dado)
listanova = sorted(lista, key = cmp_to_key(cmp_medalhas))
for i in range(n):
    print(listanova[i][0], end=" ")
    print(listanova[i][1], end=" ")
    print(listanova[i][2], end=" ")
    print(listanova[i][3])
