qtd = int(input())

for i in range(1, qtd + 1):
    values = input().split()
    val1, val2, val3 = float(values[0]), float(values[1]), float(values[2])

    media = ((val1 * 2) + (val2 * 3) + (val3 * 5)) / 10
    print("%.1f" % media)
