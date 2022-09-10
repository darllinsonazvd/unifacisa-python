n = []
x = float(input())

for i in range(100):
    if i == 0:
        metade = x
        n.insert(i, metade)
    else:
        metade /= 2
        n.insert(i, metade)

for i in range(100):
    print("N[%d] = %.4f" % (i, n[i]))
