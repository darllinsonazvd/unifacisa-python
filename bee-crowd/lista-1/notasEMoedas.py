dinheiro = float(input())

# Notas
notasDe100 = dinheiro // 100
dinheiro -= notasDe100 * 100

notasDe50 = dinheiro // 50
dinheiro -= notasDe50 * 50

notasDe20 = dinheiro // 20
dinheiro -= notasDe20 * 20

notasDe10 = dinheiro // 10
dinheiro -= notasDe10 * 10

notasDe5 = dinheiro // 5
dinheiro -= notasDe5 * 5

notasDe2 = dinheiro // 2
dinheiro -= notasDe2 * 2

# Moedas
moedasDe1R = dinheiro // 1
dinheiro -= moedasDe1R * 1
moedasDe1R = float("%.2f" % moedasDe1R)
dinheiro = float("%.2f" % dinheiro)

moedasDe50 = dinheiro // 0.50
dinheiro -= moedasDe50 * 0.50
moedasDe50 = float("%.2f" % moedasDe50)
dinheiro = float("%.2f" % dinheiro)

moedasDe25 = dinheiro // 0.25
dinheiro -= moedasDe25 * 0.25
moedasDe25 = float("%.2f" % moedasDe25)
dinheiro = float("%.2f" % dinheiro)

moedasDe10 = dinheiro // 0.10
dinheiro -= moedasDe10 * 0.10
moedasDe10 = float("%.2f" % moedasDe10)
dinheiro = float("%.2f" % dinheiro)

moedasDe5 = dinheiro // 0.05
dinheiro -= moedasDe5 * 0.05
moedasDe5 = float("%.2f" % moedasDe5)
dinheiro = float("%.2f" % dinheiro)

moedasDe1C = dinheiro / 0.01
dinheiro -= moedasDe1C * 0.01
moedasDe1C = float("%.2f" % moedasDe1C)
dinheiro = float("%.2f" % dinheiro)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % notasDe100)
print("%d nota(s) de R$ 50.00" % notasDe50)
print("%d nota(s) de R$ 20.00" % notasDe20)
print("%d nota(s) de R$ 10.00" % notasDe10)
print("%d nota(s) de R$ 5.00" % notasDe5)
print("%d nota(s) de R$ 2.00" % notasDe2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % moedasDe1R)
print("%d moeda(s) de R$ 0.50" % moedasDe50)
print("%d moeda(s) de R$ 0.25" % moedasDe25)
print("%d moeda(s) de R$ 0.10" % moedasDe10)
print("%d moeda(s) de R$ 0.05" % moedasDe5)
print("%d moeda(s) de R$ 0.01" % moedasDe1C)
