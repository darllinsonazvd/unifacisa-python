from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Claims:
    claimsIds = []

    def getClaims(self):
        self.claimsIds = []
        indexOfClaim = 1

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
                    indexOfClaim,
                    itemDB[1],
                    itemDB[2],
                    itemDB[3],
                )
            )

            self.claimsIds.append(itemDB[0])
            indexOfClaim += 1

        closeDatabase(connection)

    def addClaim(self, author: str, claim: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Reclamação", author, claim)
        insertInDatabase(connection, sqlCode, data)

        formatter.successEmitter("Reclamação adicionada com sucesso!")

        closeDatabase(connection)

    def deleteClaim(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getClaims()

        idOfClaim = validate.readInt("\nNúmero da reclamação: ")

        if idOfClaim == 0 or idOfClaim > len(self.claimsIds):
            formatter.errorEmitter("Reclamação não encontrada!")
        else:
            id = self.claimsIds[idOfClaim - 1]
            sqlCode = "DELETE FROM feedbacks WHERE id = %s"
            data = (id,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            formatter.successEmitter("Reclamação removida com sucesso!")

        closeDatabase(connection)

    def editClaim(self, idOfClaim: int):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        if idOfClaim == 0 or idOfClaim > len(self.claimsIds):
            formatter.errorEmitter("Reclamação não encontrada!")
        else:
            newClaim = validate.readString("\nDigite sua nova reclamação aqui:\n")

            id = self.claimsIds[idOfClaim - 1]
            sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
            data = (newClaim, id)
            updateDatabase(connection, sqlCode, data)

            formatter.successEmitter("Reclamação editada com sucesso!")

        closeDatabase(connection)
