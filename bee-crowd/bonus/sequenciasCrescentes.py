num = 1
result = []

while num != 0:
    num = int(input())

    for i in range(1, num + 1):
        result.append(i)
        result[i - 1] = str(result[i - 1])
        ++i

    result = " ".join(result)

    if num != 0:
        print(result)
        result = []
