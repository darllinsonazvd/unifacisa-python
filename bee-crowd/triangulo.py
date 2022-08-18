valores = input().split()

a, b, c = float(valores[0]), float(valores[1]), float(valores[2])

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((a + b) / 2) * c
    print("Area = %.1f" % area)
