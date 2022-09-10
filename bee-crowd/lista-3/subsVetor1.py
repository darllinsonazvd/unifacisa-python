x = []

for i in range(10):
    value = int(input())

    if value <= 0:
        value = 1
        x.insert(i, value)
    else:
        x.insert(i, value)

for i in range(10):
    print("X[%d] = %d" % (i, x[i]))
