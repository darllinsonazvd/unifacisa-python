n = []
value = int(input())

for i in range(10):
    n.insert(i, value)
    value *= 2

for i in range(10):
    print("N[%d] = %d" % (i, n[i]))
