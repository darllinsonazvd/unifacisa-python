print("-" * 12, "Bem-vindo ao sistema de ouvidoria da Unifacisa!", "-" * 12)

username = input("Digite seu nome: ")
userId = int(input("Digite sua matrícula: "))

claims = []  # Array de reclamações

print("\nBem-vindo %s!" % username.capitalize())
print("Matrícula: %d" % userId)

while True:
    print("-" * 75)
    print("\nSelecione uma opção:\n")
    print("1 - Listar reclamações")
    print("2 - Adicionar reclamação")
    print("3 - Remover reclamações")
    print("4 - Sair\n")
    print("-" * 75)

    option = input("Opção: ")

    if option == "1":
        print()

        if len(claims) == 0:
            print("\nNão há reclamações para exibir\n")
        else:
            for index, claim in enumerate(claims):
                print(index + 1, "|", claim)
    elif option == "2":
        claim = input("\nDigite sua reclamação:\n")
        claims.append(claim)
        print("\nReclamação adicionada com sucesso!")
    elif option == "3":
        deleteAll = input("\nDeseja apagar todas as reclamações? (s/N) ")

        if (
            deleteAll == "s"
            or deleteAll == "S"
            or deleteAll == "sim"
            or deleteAll == "Sim"
            or deleteAll == "SIM"
        ):
            claims.clear()
            print("\nTodas as reclamações foram removidas!")
        else:
            print("\nQual a reclamação que você deseja remover?\n")

            if len(claims) == 0:
                print("\nNão há reclamações para remover")
            else:
                for index, claim in enumerate(claims):
                    print(index + 1, "|", claim)

            indexOfClaim = int(input("\nNúmero da reclamação: "))

            if indexOfClaim > len(claims) or indexOfClaim <= 0:
                print("\nNão encontramos a reclamação em nosso banco de dados!\n")
            else:
                claims.pop(indexOfClaim - 1)
                print("\nReclamação removida com sucesso!\n")
    elif option == "4":
        print("\nObrigado por usar o sistema de ouvidoria da Unifacisa!")
        break
    else:
        print("\nOpção inválida")
