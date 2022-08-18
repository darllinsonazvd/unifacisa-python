from math import sqrt

pontosA = input().split(" ")
pontosB = input().split(" ")

x1, y1 = pontosA
x2, y2 = pontosB

distancia = sqrt(((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2))

print("%.4f" % distancia)
