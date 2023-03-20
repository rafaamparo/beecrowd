#2326 - Corrida

num_carros, num_voltas = map(int, input().split())
lista = []
for i in range(num_carros):
    tempo_voltas = list(map(int, input().split()))
    lista.append(sum(tempo_voltas))
tempos = sorted(lista)
print(int((lista.index(tempos[0]))+1))
print(int((lista.index(tempos[1]))+1))
print(int((lista.index(tempos[2]))+1))
