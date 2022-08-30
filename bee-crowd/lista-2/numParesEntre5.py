countNums = 1
pairs = 0

while countNums <= 5:
    num = float(input())

    if num % 2 == 0:
        pairs += 1

    countNums += 1

print("%d valores pares" % pairs)
