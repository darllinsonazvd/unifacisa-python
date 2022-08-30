qtdNums = int(input())
inInterval = 0
outOfInterval = 0

for n in range(1, qtdNums + 1):
    num = int(input())

    if num >= 10 and num <= 20:
        inInterval += 1
    else:
        outOfInterval += 1

print("%d in" % inInterval)
print("%d out" % outOfInterval)
