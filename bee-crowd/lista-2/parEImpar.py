qtdValues = int(input())

for i in range(qtdValues):
    num = int(input())

    if num % 2 == 0 and num != 0:
        if num > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif num % 2 != 0:
        if num > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
    elif num == 0:
        print("NULL")
