from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Ideas:
    ideasIds = []

    def getIdeas(self):
        self.ideasIds = []
        indexOfIdea = 1

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
                    indexOfIdea,
                    itemDB[1],
                    itemDB[2],
                    itemDB[3],
                )
            )

            self.ideasIds.append(itemDB[0])
            indexOfIdea += 1

        closeDatabase(connection)

    def addIdea(self, author: str, idea: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Ideia", author, idea)
        insertInDatabase(connection, sqlCode, data)

        formatter.successEmitter("Ideia adicionada com sucesso!")

        closeDatabase(connection)

    def deleteIdea(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getIdeas()

        idOfIdea = validate.readInt("\nNúmero da ideia: ")

        if idOfIdea == 0 or idOfIdea > len(self.ideasIds):
            formatter.errorEmitter("Ideia não encontrada!")
        else:
            id = self.ideasIds[idOfIdea - 1]
            sqlCode = "DELETE FROM feedbacks WHERE id = %s"
            data = (id,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            formatter.successEmitter("Ideia removida com sucesso!")

        closeDatabase(connection)

    def editIdea(self, idOfIdea: int):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        if idOfIdea == 0 or idOfIdea > len(self.ideasIds):
            formatter.errorEmitter("Ideia não encontrada!")
        else:
            newIdea = validate.readString("\nDigite sua nova ideia aqui:\n")

            id = self.ideasIds[idOfIdea - 1]
            sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
            data = (newIdea, id)
            updateDatabase(connection, sqlCode, data)

            formatter.successEmitter("Ideia editada com sucesso!")

        closeDatabase(connection)
