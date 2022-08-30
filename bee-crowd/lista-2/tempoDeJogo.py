start, end = map(int, input().split())

if start < end:
    time = end - start
else:
    time = (24 - start) + end

print("O JOGO DUROU %d HORA(S)" % time)
