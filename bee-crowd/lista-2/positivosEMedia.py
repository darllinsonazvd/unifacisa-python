countNums = 1
positives = 0
average = 0

while countNums <= 6:
    num = float(input())

    if num > 0:
        positives += 1
        average += num

    countNums += 1

print("%d valores positivos" % positives)
print("{:.1f}".format(average / positives))
