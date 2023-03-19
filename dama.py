#1097 - Dama

xi, yi, xii, yii = map(int, input().split())
while xi != 0 and yi != 0 and xii != 0 and yii != 0:
    dx = abs(xi - xii)
    dy = abs(yi - yii)
    if dx == 0 and dy == 0:
        print(0)
    elif dx == dy or dx == 0 or dy == 0:
        print(1)
    else:
        print(2)
    xi, yi, xii, yii = map(int, input().split())
