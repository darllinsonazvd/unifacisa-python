qtd = int(input())

for i in range(0, qtd):
    x, y = input().split()
    x = int(x)
    y = int(y)

    soma = 0

    j = 1
    while j <= y:
        if x % 2 != 0:
            soma += x
            j += 1

            x += 1
        elif x % 2 == 0:
            x += 1

    print(soma)
