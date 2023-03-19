#2242 - Huaauhahhuahau

risada = input()
res = []
vogais = ['a', 'e', 'i', 'o', 'u']
for i in range (len(risada)):
    if risada[i] in vogais:
        res.append(risada[i])
if(res == res[::-1]):
    print('S')
else:
    print('N')
