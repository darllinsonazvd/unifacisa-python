valores = input().split()

num1, num2, num3 = int(valores[0]), int(valores[1]), int(valores[2])

if num1 > num2 and num1 > num3:
    maior = num1

    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2

    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
elif num3 > num1 and num3 > num2:
    maior = num3

    if num1 > num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print(menor)
print(meio)
print(maior)
print()
print(num1)
print(num2)
print(num3)
