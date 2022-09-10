a, b, c = input().split()
lado1 = float(1)
lado2 = float(1)
lado3 = float(1)
a = float(a)
b = float(b)
c = float(c)

if a >= b and a >= c:
    lado1 = a

    if b >= c:
        lado2 = b
        lado3 = c
    else:
        lado2 = c
        lado3 = b
elif b >= a and b >= c:
    lado1 = b

    if a >= c:
        lado2 = a
        lado3 = c
    else:
        lado2 = c
        lado3 = a
elif c >= a and c >= b:
    lado1 = c

    if a >= b:
        lado2 = a
        lado3 = b
    else:
        lado2 = b
        lado3 = a
elif a == b and a == c:
    lado1 = a
    lado2 = b
    lado3 = c

a = lado1
b = lado2
c = lado3

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b != c or b == c != a or a == c != b:
        print("TRIANGULO ISOSCELES")
