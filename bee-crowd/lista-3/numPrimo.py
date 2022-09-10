qtd = int(input())

for i in range(qtd):
    num = int(input())
    cont = 0

    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1

    if cont != 2:
        print("%d nao eh primo" % num)
    elif cont == 2:
        print("%d eh primo" % num)
