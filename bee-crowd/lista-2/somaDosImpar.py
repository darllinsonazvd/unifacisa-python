qtdTests = int(input())

for i in range(qtdTests):
    values = input().split()
    x, y = int(values[0]), int(values[1])

    sumXY = 0

    if x > y:
        for num in range(y + 1, x):
            if num % 2 == 1:
                sumXY += num

    if y > x:
        for num in range(x + 1, y):
            if num % 2 == 1:
                sumXY += num

    if x == y:
        sumXY = 0

    print(sumXY)
