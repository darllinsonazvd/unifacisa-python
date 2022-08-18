idadeEmDias = int(input())

anos = idadeEmDias // 365
idadeEmDias = idadeEmDias - anos * 365

meses = idadeEmDias // 30
idadeEmDias = idadeEmDias - meses * 30

dias = idadeEmDias

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
