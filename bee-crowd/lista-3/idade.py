media = 0
contador = 0

while True:
    idade = int(input())

    if idade < 0:
        break
    else:
        media += idade
        contador += 1

print("%.2f" % (media / contador))
