dinheiro = int(input())

print(dinheiro)

# Notas
notasDe100 = dinheiro // 100
dinheiro = dinheiro - notasDe100 * 100

notasDe50 = dinheiro // 50
dinheiro = dinheiro - notasDe50 * 50

notasDe20 = dinheiro // 20
dinheiro = dinheiro - notasDe20 * 20

notasDe10 = dinheiro // 10
dinheiro = dinheiro - notasDe10 * 10

notasDe5 = dinheiro // 5
dinheiro = dinheiro - notasDe5 * 5

notasDe2 = dinheiro // 2
dinheiro = dinheiro - notasDe2 * 2

notasDe1 = dinheiro // 1
dinheiro = dinheiro - notasDe1 * 1

print("%d nota(s) de R$ 100,00" % notasDe100)
print("%d nota(s) de R$ 50,00" % notasDe50)
print("%d nota(s) de R$ 20,00" % notasDe20)
print("%d nota(s) de R$ 10,00" % notasDe10)
print("%d nota(s) de R$ 5,00" % notasDe5)
print("%d nota(s) de R$ 2,00" % notasDe2)
print("%d nota(s) de R$ 1,00" % notasDe1)
