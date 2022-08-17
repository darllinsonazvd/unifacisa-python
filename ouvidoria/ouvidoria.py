print("-" * 15, "Bem vindo ao sistema de ouvidoria da Unifacisa", "-" * 15)

claims = [
    "Bebedouro 1o andar não gela a água",
    "Computador na sala 223 deu pau",
    "Mesa quebrada",
]  # Array de reclamações

while True:
    print("\nSelecione uma opção:\n")
    print("1 - Listar reclamações")
    print("2 - Adicionar reclamação")
    print("3 - Remover reclamações")
    print("4 - Sair\n")
    print("-" * 80)

    option = int(input("Opção: "))

    if option == 1:
        print()

        if len(claims) == 0:
            print("Não há reclamações para exibir\n")
        else:
            for index, claim in enumerate(claims):
                print(index + 1, "|", claim)

        print()
    elif option == 2:
        print()

        claim = input("Digite sua reclamação:\n")
        claims.append(claim)
        print("Reclamação adicionada com sucesso!\n")
    elif option == 3:
        print()

        deleteAll = input("Deseja apagar todas as reclamações? (s/N) ")

        if (
            deleteAll == "s"
            or deleteAll == "S"
            or deleteAll == "sim"
            or deleteAll == "Sim"
            or deleteAll == "SIM"
        ):
            claims.clear()
            print("\nTodas as reclamações foram removidas!\n")
        else:
            print("\nQual a reclamação que você deseja remover?")

            if len(claims) == 0:
                print("\nNão há reclamações para remover\n")
            else:
                for index, claim in enumerate(claims):
                    print(index + 1, "|", claim)

            indexOfClaim = int(input("\nNúmero da reclamação: "))

            if indexOfClaim > len(claims) or indexOfClaim <= 0:
                print("\nNão encontramos a reclamação em nosso banco de dados!\n")
            else:
                claims.pop(indexOfClaim - 1)
                print("\nReclamação removida com sucesso!\n")
    elif option == 4:
        print()

        print("Obrigado por usar o sistema de ouvidoria da Unifacisa!")
        break
