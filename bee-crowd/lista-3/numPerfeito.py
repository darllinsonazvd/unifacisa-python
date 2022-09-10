qtd = int(input())

for i in range(qtd):
    num = int(input())

    soma = 0
    cont = 1
    while cont < num:
        if num % cont == 0:
            soma += cont
        cont += 1

    if soma == num:
        print("%d eh perfeito" % num)
    else:
        print("%d nao eh perfeito" % num)
