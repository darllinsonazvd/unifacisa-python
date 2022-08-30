qtdTests = int(input())

rabbits = 0
mouses = 0
frogs = 0

for i in range(1, qtdTests + 1):
    qtd, animal = input().split()

    if animal == "C":
        rabbits += int(qtd)
    elif animal == "R":
        mouses += int(qtd)
    elif animal == "S":
        frogs += int(qtd)

total = rabbits + mouses + frogs

percentOfRabbits = (rabbits / total) * 100
percentOfMouses = (mouses / total) * 100
percentOfFrogs = (frogs / total) * 100

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(rabbits))
print("Total de ratos: {}".format(mouses))
print("Total de sapos: {}".format(frogs))
print("Percentual de coelhos: {:.2f} %".format(percentOfRabbits))
print("Percentual de ratos: {:.2f} %".format(percentOfMouses))
print("Percentual de sapos: {:.2f} %".format(percentOfFrogs))
