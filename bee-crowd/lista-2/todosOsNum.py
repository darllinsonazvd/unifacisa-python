countNums = 1
pairs = 0
notPairs = 0
positives = 0
negatives = 0

while countNums <= 5:
    num = int(input())

    if num % 2 == 0:
        pairs += 1

    if num % 2 != 0:
        notPairs += 1

    if num > 0:
        positives += 1

    if num < 0:
        negatives += 1

    countNums += 1

print("%d valor(es) par(es)" % pairs)
print("%d valor(es) impar(es)" % notPairs)
print("%d valor(es) positivo(s)" % positives)
print("%d valor(es) negativo(s)" % negatives)
