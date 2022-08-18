valores = input().split()

a, b, c = float(valores[0]), float(valores[1]), float(valores[2])

areaTriangulo = a * c / 2
areaCirculo = 3.14159 * (c**2)
areaTrapezio = (a + b) * c / 2
areaQuadrado = b**2
areaRetangulo = a * b

print("TRIANGULO: %.3f" % areaTriangulo)
print("CIRCULO: %.3f" % areaCirculo)
print("TRAPEZIO: %.3f" % areaTrapezio)
print("QUADRADO: %.3f" % areaQuadrado)
print("RETANGULO: %.3f" % areaRetangulo)
