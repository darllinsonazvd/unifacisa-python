from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Claims:
    def getClaims(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        formatter.header("Reclamações")
        sqlCode = 'SELECT * FROM feedbacks WHERE type="Reclamação"'
        listClaims = listDatabase(connection, sqlCode)

        print(
            "{:<12} {:<15} {:<15} {:<10}\n".format(
                "Protocolo", "Tipo", "Autor", "Descrição"
            )
        )
        for itemDB in listClaims:
            print(
                "{:<12} {:<15} {:<15} {:<10}".format(
                    str(itemDB[0]), itemDB[1], itemDB[2], itemDB[3]
                )
            )

        closeDatabase(connection)

    def addClaim(self, author: str, claim: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Reclamação", author, claim)
        insertInDatabase(connection, sqlCode, data)

        print("\nReclamação adicionada com sucesso!")

        closeDatabase(connection)

    def deleteClaim(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getClaims()

        idOfClaim = validate.readInt("\nNúmero da reclamação: ")

        sqlCode = "DELETE FROM feedbacks WHERE id = %s"
        data = (idOfClaim,)
        deleteRegistryInDatabase(connection, sqlCode, data)

        print("\nReclamação removida com sucesso!\n")

        closeDatabase(connection)

    def editClaim(self, id: int, newClaim: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
        data = (newClaim, id)
        updateDatabase(connection, sqlCode, data)

        print("\nReclamação editada com sucesso!\n")

        closeDatabase(connection)
