#2233 - Etiquetas Coloridas

r = input().lower()
g = input().lower()
b = input().lower()
r = int(r, 16)
g = int(g, 16)
b = int(b, 16)
totalr = 1
totalg = int(r/g)
totalg *= totalg
totalb = int(g/b)
totalb *= totalb
totalb *= totalg
final = totalr + totalg + totalb
print(hex(final)[2:])
