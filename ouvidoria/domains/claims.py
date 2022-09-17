from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()

connection = openDatabase("localhost", "root", "root", "db_ouvidoria")


class Claims:
    def getClaims(self):
        formatter.header("Reclamações")
        sqlCode = "SELECT * FROM claims"
        listClaims = listDatabase(connection, sqlCode)

        print("Protocolo | Autor | Descrição\n")
        for itemDB in listClaims:
            print(str(itemDB[0]) + " | " + itemDB[1] + " | " + itemDB[2])

    def addClaim(self, author: str, claim: str):
        sqlCode = "INSERT INTO claims(author, claim) VALUES (%s, %s)"
        data = (author, claim)
        insertInDatabase(connection, sqlCode, data)

        print("\nReclamação adicionada com sucesso!")

    def deleteClaim(self):
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

    def editClaim(self, id: int, newClaim: str):
        sqlCode = "UPDATE claims SET claim = %s WHERE id = %s"
        data = (newClaim, id)
        updateDatabase(connection, sqlCode, data)

        print("\nReclamação editada com sucesso!\n")
