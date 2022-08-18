valores = input().split()

a, b, c = int(valores[0]), int(valores[1]), int(valores[2])

maiorAB = (a + b + abs(a - b)) / 2
maiorNum = (maiorAB + c + abs(maiorAB - c)) / 2

print("%d eh o maior" % maiorNum)
