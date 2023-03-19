#3048 - Sequência Secreta

n = int(input())
lista = []
cont = []
for i in range(n):
    lista.append(input())
for j in range(len(lista)-1):
    if lista[j] != lista[j+1]:
        cont.append(lista[j])
print(len(cont)+1)
