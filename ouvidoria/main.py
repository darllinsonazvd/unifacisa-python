from utils import *
from db.databaseOperations import *

validate = Validator()
formatter = Formatter()

connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

formatter.header("SAC Unifacisa")

username = validate.readString("Digite seu nome: ").capitalize()
userId = validate.readInt("Digite sua matrícula: ")

print("\nBem-vindo %s!" % username)
print("Matrícula: %s" % userId)

while True:
    print(formatter.line())
    print("\nSelecione uma opção:\n")
    formatter.menu(
        [
            "Listar feedbacks",
            "Adicionar feedbacks",
            "Remover feedbacks",
            "Editar feedbacks",
            "Sair",
        ]
    )
    print("\n" + formatter.line())

    option = validate.readInt("Opção: ")

    if option == 1:  # List feedbacks
        print()

        formatter.header("Reclamações")
        sqlCode = "SELECT * FROM claims"
        listClaims = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listClaims:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

        formatter.header("Ideias")
        sqlCode = "SELECT * FROM ideas"
        listIdeas = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listIdeas:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

        formatter.header("Outros feedbacks")
        sqlCode = "SELECT * FROM othersFeedbacks"
        listOthers = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listOthers:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])
    elif option == 2:  # Add feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Outro"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            claim = validate.readString("\nDigite sua reclamação:\n")

            sqlCode = "INSERT INTO claims(author, claim) VALUES (%s, %s)"
            data = (username, claim)
            insertInDatabase(connection, sqlCode, data)

            print("\nReclamação adicionada com sucesso!")
        elif category == 2:
            idea = validate.readString("\nDigite sua ideia:\n")

            sqlCode = "INSERT INTO ideas(author, idea) VALUES (%s, %s)"
            data = (username, idea)
            insertInDatabase(connection, sqlCode, data)

            print("\nIdeia adicionada com sucesso!")
        elif category == 3:
            other = validate.readString("\nDigite seu feedback:\n")

            sqlCode = "INSERT INTO othersFeedbacks(author, feedback) VALUES (%s, %s)"
            data = (username, other)
            insertInDatabase(connection, sqlCode, data)

            print("\nFeedback adicionado com sucesso!")
        else:
            print("\nCategoria não encontrada!\n")
    elif option == 3:  # Remove feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Outro"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            print("\nQual a reclamação que você deseja remover?\n")

            sqlCode = "SELECT * FROM claims"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfClaim = validate.readInt("\nNúmero da reclamação: ")

            sqlCode = "DELETE FROM claims WHERE id = %s"
            data = (idOfClaim,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nReclamação removida com sucesso!\n")
        elif category == 2:
            print("\nQual a ideia que você deseja remover?\n")

            sqlCode = "SELECT * FROM ideas"
            listIdeas = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listIdeas:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfIdea = validate.readInt("\nNúmero da ideia: ")

            sqlCode = "DELETE FROM ideas WHERE id = %s"
            data = (idOfIdea,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nIdeia removida com sucesso!\n")
        elif category == 3:
            print("\nQual o feedback que você deseja remover?\n")

            sqlCode = "SELECT * FROM othersFeedbacks"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfFeedback = validate.readInt("\nNúmero da ideia: ")

            sqlCode = "DELETE FROM othersFeedbacks WHERE id = %s"
            data = (idOfFeedback,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            print("\nFeedback removido com sucesso!\n")
    elif option == 4:  # Edit feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Outro"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            print("\nQual a reclamação que você deseja editar?\n")

            sqlCode = "SELECT * FROM claims"
            listClaims = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listClaims:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfClaim = validate.readInt("\nNúmero da reclamação: ")
            newClaim = validate.readString("\nDigite sua nova reclamação aqui:\n")

            sqlCodeUpdate = "UPDATE claims SET claim = %s WHERE id = %s"
            data = (newClaim, idOfClaim)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nReclamação editada com sucesso!\n")
        elif category == 2:
            print("\nQual a ideia que você deseja editar?\n")

            sqlCode = "SELECT * FROM ideas"
            listIdeas = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listIdeas:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfIdea = validate.readInt("\nNúmero da ideia: ")
            newIdea = validate.readString("\nDigite sua nova ideia aqui:\n")

            sqlCodeUpdate = "UPDATE ideas SET idea = %s WHERE id = %s"
            data = (newIdea, idOfIdea)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nIdeia editada com sucesso!\n")
        elif category == 3:
            print("\nQual o feedback que você deseja editar?\n")

            sqlCode = "SELECT * FROM othersFeedbacks"
            listOthers = listDatabase(connection, sqlCode)

            print("Protocolo | Autor | Descrição")
            for itemDB in listOthers:
                print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

            idOfFeedback = validate.readInt("\nNúmero do feedback: ")
            newFeedback = validate.readString("\nDigite seu novo feedback aqui:\n")

            sqlCodeUpdate = "UPDATE othersFeedbacks SET feedback = %s WHERE id = %s"
            data = (newFeedback, idOfFeedback)
            updateDatabase(connection, sqlCodeUpdate, data)

            print("\nFeedback editado com sucesso!\n")
    elif option == 5:  # Quit
        closeDatabase(connection)
        print("\nObrigado por usar o sistema de ouvidoria da Unifacisa!")
        break
    else:  # Error handling
        print("\nOpção inválida")
