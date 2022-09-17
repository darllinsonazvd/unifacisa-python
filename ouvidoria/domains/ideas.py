from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()

connection = openDatabase("localhost", "root", "root", "db_ouvidoria")


class Ideas:
    def getIdeas(self):
        formatter.header("Ideias")
        sqlCode = "SELECT * FROM ideas"
        listIdeas = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listIdeas:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

    def addIdeas(self, author: str, idea: str):
        sqlCode = "INSERT INTO ideas(author, idea) VALUES (%s, %s)"
        data = (author, idea)
        insertInDatabase(connection, sqlCode, data)

        print("\nIdeia adicionada com sucesso!")

    def deleteIdea(self):
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

    def editIdea(self, id: int, newIdea: str):
        sqlCode = "UPDATE ideas SET idea = %s WHERE id = %s"
        data = (newIdea, id)
        updateDatabase(connection, sqlCode, data)

        print("\nIdeia editada com sucesso!\n")
