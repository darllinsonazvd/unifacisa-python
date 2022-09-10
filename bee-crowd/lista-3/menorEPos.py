tamanho = int(input())
x = input().split()

for i in range(tamanho):
    x[i] = int(x[i])

menor = x[0]
posicao = 0

for j in range(1, tamanho):
    if x[j] < menor:
        menor = x[j]
        posicao = j

print("Menor valor: %d" % menor)
print("Posicao: %d" % posicao)
