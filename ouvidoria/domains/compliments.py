from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Compliments:
    def getCompliments(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        formatter.header("Elogios")
        sqlCode = 'SELECT * FROM feedbacks WHERE type="Elogio"'
        listCompliments = listDatabase(connection, sqlCode)

        print("Protocolo | Tipo | Autor | Descrição\n")
        for itemDB in listCompliments:
            print(
                str(itemDB[0])
                + " | "
                + itemDB[1]
                + " | "
                + itemDB[2]
                + " | "
                + itemDB[3]
            )

        closeDatabase(connection)

    def addCompliment(self, author: str, compliment: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Elogio", author, compliment)
        insertInDatabase(connection, sqlCode, data)

        print("\nElogio adicionado com sucesso!")

        closeDatabase(connection)

    def deleteCompliment(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getCompliments()

        idOfCompliment = validate.readInt("\nNúmero do elogio: ")

        sqlCode = "DELETE FROM feedbacks WHERE id = %s"
        data = (idOfCompliment,)
        deleteRegistryInDatabase(connection, sqlCode, data)

        print("\nElogio removido com sucesso!\n")

        closeDatabase(connection)

    def editCompliment(self, id: int, newCompliment: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
        data = (newCompliment, id)
        updateDatabase(connection, sqlCode, data)

        print("\nElogio editado com sucesso!\n")

        closeDatabase(connection)
