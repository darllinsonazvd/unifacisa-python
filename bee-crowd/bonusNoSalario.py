nome = input()
salarioFixo = float(input())
vendasEmDinheiro = float(input())
comissao = vendasEmDinheiro * 0.15

salarioFinal = salarioFixo + comissao

print("TOTAL = R$ %.2f" % salarioFinal)
