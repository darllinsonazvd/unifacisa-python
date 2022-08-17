entrada = input().split(" ")

opcao, qtd = entrada

if opcao == "1":
    print("Total: R$ {:.2f}".format(4.00 * float(qtd)))
elif opcao == "2":
    print("Total: R$ {:.2f}".format(4.50 * float(qtd)))
elif opcao == "3":
    print("Total: R$ {:.2f}".format(5.00 * float(qtd)))
elif opcao == "4":
    print("Total: R$ {:.2f}".format(2.00 * float(qtd)))
elif opcao == "5":
    print("Total: R$ {:.2f}".format(1.50 * float(qtd)))
