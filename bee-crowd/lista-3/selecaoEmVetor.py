a = []

for i in range(100):
    num = float(input())
    a.append(num)

    if num <= 10.0:
        print("A[%d] = %.1f" % (i, num))
