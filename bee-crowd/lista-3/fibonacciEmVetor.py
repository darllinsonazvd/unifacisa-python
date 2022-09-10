qtd = int(input())

for i in range(qtd):
    num = int(input())
    fibonacci = [0, 1]
    if num > 1:
        for j in range(2, num + 1):
            fibonacci.append(fibonacci[j - 2] + fibonacci[j - 1])

        print("Fib(%d) = %d" % (num, fibonacci[num]))
    elif num <= 1:
        print("Fib(%d) = %d" % (num, fibonacci[num]))
