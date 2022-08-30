num = int(input())

for n in range(1, num + 1):
    result = n**2

    if (n % 2) == 0:
        print("{}^2 = {}".format(n, result))
