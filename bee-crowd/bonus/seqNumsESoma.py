soma = 0
j = 0

while j != 1:
    m, n = input().split()
    m = int(m)
    n = int(n)

    soma = 0

    if m > n:
        temp = m  # Variável temporária

        m = n
        n = temp

    if m <= 0 or n <= 0:
        j = 1

    if j != 1:
        for i in range(m, n + 1):
            print("%d " % (i), end="")
            soma += i
            if i == n:
                print("Sum=%d" % (soma))
