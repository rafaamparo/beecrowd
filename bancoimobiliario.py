#2304 - Banco Imobiliário

quantia, n_operaçoes = map(int, input().split())
D = quantia
E = quantia
F = quantia
for i in range(n_operaçoes):
    operaçao = input().split()
    if operaçao[0].upper() == 'C':
        if operaçao[1].upper() == 'D':
            D -= int(operaçao[2])
        elif operaçao[1].upper() == 'E':
            E -= int(operaçao[2])
        else:
            F -= int(operaçao[2])
    if operaçao[0].upper() == 'V':
        if operaçao[1].upper() == 'D':
            D += int(operaçao[2])
        elif operaçao[1].upper() == 'E':
            E += int(operaçao[2])
        else:
            F += int(operaçao[2])
    if operaçao[0].upper() == 'A':
        if operaçao[1].upper() == 'D' and operaçao[2].upper() == 'E':
            D += int(operaçao[3])
            E -= int(operaçao[3])
        elif operaçao[1].upper() == 'D' and operaçao[2].upper() == 'F':
            D += int(operaçao[3])
            F -= int(operaçao[3])
        elif operaçao[1].upper() == 'E' and operaçao[2].upper() == 'D':
            E += int(operaçao[3])
            D -= int(operaçao[3])
        elif operaçao[1].upper() == 'E' and operaçao[2].upper() == 'F':
            E += int(operaçao[3])
            F -= int(operaçao[3])
        elif operaçao[1].upper() == 'F' and operaçao[2].upper() == 'D':
            F += int(operaçao[3])
            D -= int(operaçao[3])
        else:
            F += int(operaçao[3])
            E -= int(operaçao[3])
print(D, E, F)
