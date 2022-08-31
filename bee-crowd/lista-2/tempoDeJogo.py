startHour, startMinute, endHour, endMinute = map(int, input().split())

if startHour < endHour:
    hours = endHour - startHour

    if startMinute < endMinute:
        minutes = endMinute - startMinute
    elif startMinute > endMinute:
        hours -= 1
        minutes = (60 - startMinute) + endMinute
    elif startMinute == endMinute:
        minutes = 0
elif endHour < startHour:
    hours = (24 - startHour) + endHour

    if startMinute < endMinute:
        minutes = endMinute - startMinute
    elif startMinute > endMinute:
        hours -= 1
        minutes = (60 - startMinute) + endMinute
    elif startMinute == endMinute:
        minutes = 0
elif startHour == endHour:
    if startMinute < endMinute:
        hours = 0
        minutes = endMinute - startMinute
    elif startMinute > endMinute:
        hours = 23
        minutes = (60 - startMinute) + endMinute
    elif startMinute == endMinute:
        hours = 24
        minutes = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))

# Sem minutos

""" if start < end:
    time = end - start
else:
    time = (24 - start) + end

print("O JOGO DUROU %d HORA(S)" % time) """
