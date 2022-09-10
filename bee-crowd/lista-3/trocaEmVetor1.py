n = []

for i in range(20):
    valor = int(input())
    n.append(valor)

pos = 0

for elm in n[::-1]:
    print("N[%d] = %d" % (pos, elm))
    pos += 1
