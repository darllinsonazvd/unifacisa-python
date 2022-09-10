a, b = input().split()
a = int(a)
b = int(b)

for r in range(abs(b)):
    if (a - r) % b == 0:
        q = int((a - r) / b)
        break

print(q, r)
