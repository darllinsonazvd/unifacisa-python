dayI = input().split()
hourI = input().split()

dayF = input().split()
hourF = input().split()

initialDay, finalDay = int(dayI[1]), int(dayF[1])
initialHour, initialMinutes, initialSeconds = (
    int(hourI[0]),
    int(hourI[2]),
    int(hourI[4]),
)
finalHour, finalMinutes, finalSeconds = int(hourF[0]), int(hourF[2]), int(hourF[4])

minutesInSeconds = 60
hoursInSeconds = minutesInSeconds * 60
dayInSeconds = hoursInSeconds * 24

start = (
    initialSeconds
    + initialMinutes * minutesInSeconds
    + initialHour * hoursInSeconds
    + initialDay * dayInSeconds
)
end = (
    finalSeconds
    + finalMinutes * minutesInSeconds
    + finalHour * hoursInSeconds
    + finalDay * dayInSeconds
)

if start < end:
    time = end - start
    days = int(time / dayInSeconds)
    time = time % dayInSeconds
    hours = int(time / hoursInSeconds)
    time = time % hoursInSeconds
    minutes = int(time / minutesInSeconds)
    time = time % minutesInSeconds
    seconds = time

    print("%d dia(s)" % days)
    print("%d hora(s)" % hours)
    print("%d minuto(s)" % minutes)
    print("%d segundo(s)" % seconds)
