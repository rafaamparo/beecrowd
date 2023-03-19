#problema 2366 - Maratona

S = True
d = 0
n, m = map(int, input().split())
p =  list(map(int, input().split()))
for i in range(n):
    if i < (n-1):
        d = p[i+1] - p[i]
        if d > m:
            S = False
    else:
        d = 42195 - p[i]
        if d > m:
            S = False
if S:
    print('S')
else:
    print('N')
