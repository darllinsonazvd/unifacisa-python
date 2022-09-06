from utils.databaseOperations import *

connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

print("-" * 12, "Bem-vindo ao sistema de ouvidoria da Unifacisa!", "-" * 12)

username = input("Digite seu nome: ").capitalize()
userId = int(input("Digite sua matrícula: "))

print("\nBem-vindo %s!" % username)
print("Matrícula: %s" % userId)

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

        print("\nReclamações:\n")
        sqlCode = "SELECT * FROM claims"
        listClaims = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listClaims:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

        print("\nIdeias:\n")
        sqlCode = "SELECT * FROM ideas"
        listIdeas = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listIdeas:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

        print("\nOutros:\n")
        sqlCode = "SELECT * FROM othersFeedbacks"
        listOthers = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listOthers:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])
    elif option == "2":  # Add feedbacks
        print("\nCategorias:\n")
        print("1 - Reclamação")
        print("2 - Ideia")
        print("3 - Outro")

        category = input("Qual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == "1":
            claim = input("\nDigite sua reclamação:\n")

            sqlCode = "INSERT INTO claims(author, claim) VALUES (%s, %s)"
            data = (username, claim)
            insertInDatabase(connection, sqlCode, data)

            print("\nReclamação adicionada com sucesso!")
        elif category == "2":
            idea = input("\nDigite sua ideia:\n")

            sqlCode = "INSERT INTO ideas(author, idea) VALUES (%s, %s)"
            data = (username, idea)
            insertInDatabase(connection, sqlCode, data)

            print("\nIdeia adicionada com sucesso!")
        elif category == "3":
            other = input("\nDigite seu feedback:\n")

            sqlCode = "INSERT INTO othersFeedbacks(author, feedback) VALUES (%s, %s)"
            data = (username, other)
            insertInDatabase(connection, sqlCode, data)

            print("\nFeedback adicionado com sucesso!")
        else:
            print("\nCategoria não encontrada!\n")
    elif option == "3":  # Remove feedbacks
        print("\nCategorias:\n")
        print("1 - Reclamação")
        print("2 - Ideia")
        print("3 - Outro")

        category = input(
            "Qual a categoria do feedback que deseja remover? (1 / 2 / 3) "
        )

        if category == "1":
            print("\nQual a reclamação que você deseja remover?\n")

            sqlCode = "SELECT * FROM claims"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfClaim = int(input("\nNúmero da reclamação: "))

            sqlCode = "DELETE FROM claims WHERE id = %s"
            data = (idOfClaim,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nReclamação removida com sucesso\n")
        elif category == "2":
            print("\nQual a ideia que você deseja remover?\n")

            sqlCode = "SELECT * FROM ideas"
            listIdeas = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listIdeas:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfIdeas = int(input("\nNúmero da ideia: "))

            sqlCode = "DELETE FROM ideas WHERE id = %s"
            data = (idOfIdeas,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nIdeia removida com sucesso\n")
        elif category == "3":
            print("\nQual o feedback que você deseja remover?\n")

            sqlCode = "SELECT * FROM othersFeedbacks"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfFeedback = int(input("\nNúmero do feedback: "))

            sqlCode = "DELETE FROM othersFeedbacks WHERE id = %s"
            data = (idOfFeedback,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nFeedback removido com sucesso\n")
    elif option == "4":  # Edit feedbacks
        print("\nCategorias:\n")
        print("1 - Reclamação")
        print("2 - Ideia")
        print("3 - Outro")

        category = input("Qual a categoria do feedback que deseja editar? (1 / 2 / 3) ")

        if category == "1":
            print("\nQual a reclamação que você deseja editar?\n")

            sqlCode = "SELECT * FROM claims"
            listClaims = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listClaims:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfClaim = int(input("\nNúmero da reclamação: "))
            newClaim = input("\nDigite sua nova reclamação aqui:\n")

            sqlCodeUpdate = "UPDATE claims SET claim = %s WHERE id = %s"
            data = (newClaim, idOfClaim)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nReclamação editada com sucesso\n")
        elif category == "2":
            print("\nQual a ideia que você deseja editar?\n")

            sqlCode = "SELECT * FROM ideas"
            listIdeas = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listIdeas:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfIdea = int(input("\nNúmero da ideia: "))
            newIdea = input("\nDigite sua nova ideia aqui:\n")

            sqlCodeUpdate = "UPDATE ideas SET idea = %s WHERE id = %s"
            data = (newIdea, idOfIdea)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nIdeia editada com sucesso\n")
        elif category == "3":
            print("\nQual o feedback que você deseja editar?\n")

            sqlCode = "SELECT * FROM othersFeedbacks"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfFeedback = int(input("\nNúmero do feedback: "))
            newFeedback = input("\nDigite seu novo feedback aqui:\n")

            sqlCodeUpdate = "UPDATE othersFeedbacks SET feedback = %s WHERE id = %s"
            data = (newFeedback, idOfFeedback)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nIdeia editada com sucesso\n")
    elif option == "5":  # Quit
        closeDatabase(connection)
        print("\nObrigado por usar o sistema de ouvidoria da Unifacisa!")
        break
    else:  # Error handling
        print("\nOpção inválida")
