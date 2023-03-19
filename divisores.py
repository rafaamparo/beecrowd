#2238 - Divisores

resultado = -1
a, b, c, d = map(int, input().split())
if (a != b and c != d):
    n = a
    m = c
    while (n <= m):
        if (n % a == 0 and n % b != 0 and c % n == 0 and d % n != 0):
            resultado = n
            break
        n += a
print(resultado)
