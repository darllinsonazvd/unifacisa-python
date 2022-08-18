valores = input().split()

a, b, c, d = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
