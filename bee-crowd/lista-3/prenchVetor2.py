n = []
t = int(input())

for i in range(1000):
    j = 0
    while j < t:
        n.append(j)
        j += 1

    print("N[%d] = %d" % (i, n[i]))
