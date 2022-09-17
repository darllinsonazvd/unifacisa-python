from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()

connection = openDatabase("localhost", "root", "root", "db_ouvidoria")


class OthersFeedbacks:
    def getOthersFeedbacks(self):
        formatter.header("Outros feedbacks")
        sqlCode = "SELECT * FROM othersFeedbacks"
        listOthers = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listOthers:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

    def addOtherFeedback(self, author: str, feedback: str):
        sqlCode = "INSERT INTO othersFeedbacks(author, feedback) VALUES (%s, %s)"
        data = (author, feedback)
        insertInDatabase(connection, sqlCode, data)

        print("\nFeedback adicionado com sucesso!")

    def deleteOtherFeedback(self):
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

    def editOtherFeedback(self, id: int, newFeedback: str):
        sqlCode = "UPDATE othersFeedbacks SET feedback = %s WHERE id = %s"
        data = (newFeedback, id)
        updateDatabase(connection, sqlCode, data)

        print("\nFeedback editado com sucesso!\n")
