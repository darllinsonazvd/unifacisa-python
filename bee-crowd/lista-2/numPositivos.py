countNums = 1
positives = 0

while countNums <= 6:
    num = float(input())

    if num > 0:
        positives += 1

    countNums += 1

print("%d valores positivos" % positives)
