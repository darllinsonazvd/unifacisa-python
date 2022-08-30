num1 = int(input())
num2 = int(input())

sumNums = 0

if num1 > num2:
    for n in range(num2 + 1, num1):
        if n % 2 != 0:
            sumNums += n
elif num1 < num2:
    for n in range(num1 + 1, num2):
        if n % 2 != 0:
            sumNums += n
elif num1 == num2:
    sumNums = 0

print(sumNums)
