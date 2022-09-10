novaConta = "n"

while novaConta == "n":
    cont = 0
    media = 0
    respostaNovaConta = 3

    while cont < 2:
        num = float(input())
        if 0 <= num <= 10:
            cont += 1
            media += num
        else:
            print("nota invalida")

    print("media = %.2f" % (media / 2))

    while respostaNovaConta != 1 and respostaNovaConta != 2:
        respostaNovaConta = int(input("novo calculo (1-sim 2-nao)\n"))

        if respostaNovaConta == 1:
            novaConta = "n"
        elif respostaNovaConta == 2:
            novaConta = "s"
        else:
            respostaNovaConta = int(input("novo calculo (1-sim 2-nao)\n"))
