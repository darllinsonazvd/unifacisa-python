x = 1
soma = 0

for i in range(1, 40, 2):
    result = i / x
    soma = soma + result
    x = x * 2

print("%.2f" % soma)
