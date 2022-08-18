tempoEmSegundos = int(input())

horas = tempoEmSegundos // 3600
tempoEmSegundos = tempoEmSegundos - horas * 3600

minutos = tempoEmSegundos // 60
tempoEmSegundos = tempoEmSegundos - minutos * 60

segundos = tempoEmSegundos

print("{}:{}:{}".format(horas, minutos, segundos))
