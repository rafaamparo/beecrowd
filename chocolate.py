#2328 - Chocolate

num_divisoes = int(input())
pedacos = list(map(int, input().split()))
soma = sum(pedacos)
result = int(soma) - num_divisoes
print(result)
