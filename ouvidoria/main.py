from utils.databaseOperations import *

print("-" * 12, "Bem-vindo ao sistema de ouvidoria da Unifacisa!", "-" * 12)

username = input("Digite seu nome: ")
userId = int(input("Digite sua matrícula: "))

feedbacks = {"claims": [], "ideas": [], "others": []}

print("\nBem-vindo %s!" % username.capitalize())
print("Matrícula: %d" % userId)

while True:
    print("-" * 75)
    print("\nSelecione uma opção:\n")
    print("1 - Listar feedbacks")
    print("2 - Adicionar feedback")
    print("3 - Remover feedbacks")
    print("4 - Editar feedbacks")
    print("5 - Sair\n")
    print("-" * 75)

    option = input("Opção: ")

    if option == "1":  # List feedbacks
        print()

        if (
            len(feedbacks["claims"]) == 0
            and len(feedbacks["ideas"]) == 0
            and len(feedbacks["others"]) == 0
        ):
            print("\nNão há feedbacks para exibir")
        else:
            print("\nReclamações:")
            print("\nNão há reclamações" if len(feedbacks["claims"]) == 0 else "")
            for index, claim in enumerate(feedbacks["claims"]):
                print(index + 1, "|", claim)

            print("\nIdeias:")
            print("\nNão há ideias" if len(feedbacks["ideas"]) == 0 else "")
            for index, idea in enumerate(feedbacks["ideas"]):
                print(index + 1, "|", idea)

            print("\nOutros:")
            print("\nNão há outros feedbacks" if len(feedbacks["others"]) == 0 else "")
            for index, other in enumerate(feedbacks["others"]):
                print(index + 1, "|", other)
    elif option == "2":  # Add feedbacks
        print("\nCategorias:\n")
        print("1 - Reclamação")
        print("2 - Ideia")
        print("3 - Outro")

        category = input("Qual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == "1":
            claim = input("\nDigite sua reclamação:\n")
            feedbacks["claims"].append(claim)
            print("\nReclamação adicionada com sucesso!")
        elif category == "2":
            idea = input("\nDigite sua ideia:\n")
            feedbacks["ideas"].append(idea)
            print("\nIdeia adicionada com sucesso!")
        elif category == "3":
            other = input("\nDigite seu feedback:\n")
            feedbacks["others"].append(other)
            print("\nFeedback adicionado com sucesso!")
        else:
            print("\nCategoria não encontrada!\n")
    elif option == "3":  # Remove feedbacks
        deleteAll = input("\nDeseja apagar todas os feedbacks? (s/N) ")

        if deleteAll == "s" or deleteAll == "S":
            feedbacks["claims"].clear()
            feedbacks["ideas"].clear()
            feedbacks["others"].clear()
            print("\nTodas os feedbacks foram removidos!")
        else:
            print("\nCategorias:\n")
            print("1 - Reclamação")
            print("2 - Ideia")
            print("3 - Outro")

            category = input(
                "Qual a categoria do feedback que deseja remover? (1 / 2 / 3) "
            )

            if category == "1":
                print("\nQual a reclamação que você deseja remover?\n")

                if len(feedbacks["claims"]) == 0:
                    print("\nNão há reclamações para remover")
                else:
                    for index, claim in enumerate(feedbacks["claims"]):
                        print(index + 1, "|", claim)

                indexOfClaim = int(input("\nNúmero da reclamação: "))

                if indexOfClaim > len(feedbacks["claims"]) or indexOfClaim <= 0:
                    print("\nNão encontramos a reclamação em nosso banco de dados!\n")
                else:
                    feedbacks["claims"].pop(indexOfClaim - 1)
                    print("\nReclamação removida com sucesso!\n")
            elif category == "2":
                print("\nQual a ideia que você deseja remover?\n")

                if len(feedbacks["ideas"]) == 0:
                    print("\nNão há ideias para remover")
                else:
                    for index, idea in enumerate(feedbacks["ideas"]):
                        print(index + 1, "|", idea)

                indexOfIdea = int(input("\nNúmero da ideia: "))

                if indexOfIdea > len(feedbacks["ideas"]) or indexOfIdea <= 0:
                    print("\nNão encontramos a ideia em nosso banco de dados!\n")
                else:
                    feedbacks["ideas"].pop(indexOfIdea - 1)
                    print("\nIdeia removida com sucesso!\n")
            elif option == "3":
                print("\nQual o feedback que você deseja remover?\n")

                if len(other) == 0:
                    print("\nNão há feedbacks para remover")
                else:
                    for index, other in enumerate(feedbacks["others"]):
                        print(index + 1, "|", other)

                indexOfOther = int(input("\nNúmero do feedback: "))

                if indexOfOther > len(feedbacks["others"]) or indexOfOther <= 0:
                    print("\nNão encontramos o feedback em nosso banco de dados!\n")
                else:
                    feedbacks["others"].pop(indexOfOther - 1)
                    print("\nFeedback removido com sucesso!\n")
    elif option == "4":  # Edit feedbacks
        print("\nCategorias:\n")
        print("1 - Reclamação")
        print("2 - Ideia")
        print("3 - Outro")

        category = input("Qual a categoria do feedback que deseja editar? (1 / 2 / 3) ")

        if category == "1":
            print("\nQual a reclamação que você deseja editar?\n")

            if len(feedbacks["claims"]) == 0:
                print("\nNão há reclamações para editar")
            else:
                for index, claim in enumerate(feedbacks["claims"]):
                    print(index + 1, "|", claim)

            indexOfClaim = int(input("\nNúmero da reclamação: "))

            if indexOfClaim > len(feedbacks["claims"]) or indexOfClaim <= 0:
                print("\nNão encontramos a reclamação em nosso banco de dados!\n")
            else:
                newClaim = input("\nDigite sua nova reclamação aqui:\n")
                feedbacks["claims"][indexOfClaim - 1] = newClaim
                print("\nReclamação editada com sucesso!\n")
        elif category == "2":
            print("\nQual a ideia que você deseja editar?\n")

            if len(feedbacks["ideas"]) == 0:
                print("\nNão há ideias para editar")
            else:
                for index, idea in enumerate(feedbacks["ideas"]):
                    print(index + 1, "|", idea)

            indexOfIdea = int(input("\nNúmero da ideia: "))

            if indexOfIdea > len(feedbacks["ideas"]) or indexOfIdea <= 0:
                print("\nNão encontramos a ideia em nosso banco de dados!\n")
            else:
                newIdea = input("\nDigite sua nova ideia aqui:\n")
                feedbacks["ideas"][indexOfIdea - 1] = newIdea
                print("\nIdeia editada com sucesso!\n")
        elif category == "3":
            print("\nQual o feedback que você deseja editar?\n")

            if len(feedbacks["others"]) == 0:
                print("\nNão há outros feedbacks para editar")
            else:
                for index, other in enumerate(feedbacks["others"]):
                    print(index + 1, "|", other)

            indexOfOther = int(input("\nNúmero do feedback: "))

            if indexOfOther > len(other) or indexOfOther <= 0:
                print("\nNão encontramos o feedback em nosso banco de dados!\n")
            else:
                newFeedback = input("\nDigite seu novo feedback aqui:\n")
                feedbacks["others"][indexOfOther - 1] = newFeedback
                print("\nFeedback editado com sucesso!\n")
    elif option == "5":  # Quit
        print("\nObrigado por usar o sistema de ouvidoria da Unifacisa!")
        break
    else:  # Error handling
        print("\nOpção inválida")
