salary = float(input())

if salary <= 2000.0:
    tax = 0
    print("Isento")
elif 2000.01 <= salary <= 3000.0:
    tax8 = salary - 2000.0
    finalTax = tax8 * (8 / 100)
elif 3000.01 <= salary <= 4500.0:
    tax8 = (8 / 100) * (1000.0)
    tax18 = salary - 3000.0
    finalTax = tax18 * (18 / 100) + tax8
elif salary >= 4500.01:
    tax8 = (8 / 100) * (1000.0)
    tax18 = (18 / 100) * (1500.0)
    tax28 = salary - 4500.0
    finalTax = tax8 + tax18 + tax28 * (28 / 100)

if salary > 2000.0:
    finalTax = float(finalTax)
    print("R$ %.2f" % finalTax)
