salary = float(input())

if salary <= 400.00:
    newSalary = salary * 1.15
    readjustment = newSalary - salary
    percent = 15
elif 400.01 <= salary <= 800.00:
    newSalary = salary * 1.12
    readjustment = newSalary - salary
    percent = 12
elif 800.01 <= salary <= 1200.00:
    newSalary = salary * 1.10
    readjustment = newSalary - salary
    percent = 10
elif 1200.01 <= salary <= 2000.00:
    newSalary = salary * 1.07
    readjustment = newSalary - salary
    percent = 7
elif salary > 2000.00:
    newSalary = salary * 1.04
    readjustment = newSalary - salary
    percent = 4

print("Novo salario: {:.2f}".format(newSalary))
print("Reajuste ganho: {:.2f}".format(readjustment))
print("Em percentual: {} %".format(percent))
