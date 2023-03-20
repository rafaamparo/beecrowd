#2321 - Detectando Colisões
# ! WRONG ANSWER (5%)! 🤷

rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))
if (rect2[2] <= rect1[2] and rect2[2] >= rect1[0]) or (rect2[3] <= rect1[3] and rect2[3] >= rect1[1]) or (rect2[0] <= rect1[2] and rect2[0] >= rect1[0]) or (rect2[1] <= rect1[3] and rect2[1] >= rect1[1]):
    print('1')
else:
    print('0')
