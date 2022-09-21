from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Ideas:
    def getIdeas(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        formatter.header("Ideias")
        sqlCode = 'SELECT * FROM feedbacks WHERE type="Ideia"'
        listIdeas = listDatabase(connection, sqlCode)

        print(
            "{:<12} {:<15} {:<15} {:<10}\n".format(
                "Protocolo", "Tipo", "Autor", "Descrição"
            )
        )
        for itemDB in listIdeas:
            print(
                "{:<12} {:<15} {:<15} {:<10}".format(
                    str(itemDB[0]), itemDB[1], itemDB[2], itemDB[3]
                )
            )

        closeDatabase(connection)

    def addIdea(self, author: str, idea: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Ideia", author, idea)
        insertInDatabase(connection, sqlCode, data)

        print("\nIdeia adicionada com sucesso!")

        closeDatabase(connection)

    def deleteIdea(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getIdeas()

        idOfIdea = validate.readInt("\nNúmero da ideia: ")

        sqlCode = "DELETE FROM feedbacks WHERE id = %s"
        data = (idOfIdea,)
        deleteRegistryInDatabase(connection, sqlCode, data)

        print("\nIdeia removida com sucesso!\n")

        closeDatabase(connection)

    def editIdea(self, id: int, newIdea: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
        data = (newIdea, id)
        updateDatabase(connection, sqlCode, data)

        print("\nIdeia editada com sucesso!\n")

        closeDatabase(connection)
