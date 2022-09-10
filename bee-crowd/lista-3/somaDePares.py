while True:
    x = int(input())

    soma = 0
    i = 1

    if x != 0:
        while i <= 5:
            if x % 2 == 0:
                soma += x
                x += 1
                i += 1
            else:
                x += 1

        print(soma)
    elif x == 0:
        break
