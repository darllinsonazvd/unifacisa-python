from db.databaseOperations import *
from utils import *

validate = Validator()
formatter = Formatter()


class Compliments:
    ideasIds = []
    ideasTypes = []
    ideasAuthors = []
    ideasDescriptions = []

    def getCompliments(self):
        self.complimentsIds = []
        self.complimentsTypes = []
        self.complimentsAuthors = []
        self.complimentsDescriptions = []

        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        formatter.header("Elogios")
        sqlCode = 'SELECT * FROM feedbacks WHERE type="Elogio"'
        listCompliments = listDatabase(connection, sqlCode)

        print(
            "{:<12} {:<15} {:<15} {:<10}\n".format(
                "Protocolo", "Tipo", "Autor", "Descrição"
            )
        )
        for itemDB in listCompliments:
            self.complimentsIds.append(itemDB[0])
            self.complimentsTypes.append(itemDB[1])
            self.complimentsAuthors.append(itemDB[2])
            self.complimentsDescriptions.append(itemDB[3])
        for i in range(len(self.complimentsIds)):
            print(
                "{:<12} {:<15} {:<15} {:<10}".format(
                    i + 1,
                    self.complimentsTypes[i],
                    self.complimentsAuthors[i],
                    self.complimentsDescriptions[i],
                )
            )

        closeDatabase(connection)

    def addCompliment(self, author: str, compliment: str):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        sqlCode = "INSERT INTO feedbacks(type, author, feedback) VALUES (%s, %s, %s)"
        data = ("Elogio", author, compliment)
        insertInDatabase(connection, sqlCode, data)

        formatter.successEmitter("Elogio adicionado com sucesso!")

        closeDatabase(connection)

    def deleteCompliment(self):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        self.getCompliments()

        idOfCompliment = validate.readInt("\nNúmero do elogio: ")

        if idOfCompliment == 0 or idOfCompliment > len(self.complimentsIds):
            formatter.errorEmitter("Elogio não encontrado!")
        else:
            id = self.complimentsIds[idOfCompliment - 1]
            sqlCode = "DELETE FROM feedbacks WHERE id = %s"
            data = (id,)
            deleteRegistryInDatabase(connection, sqlCode, data)

            formatter.successEmitter("Elogio removido com sucesso!")

        closeDatabase(connection)

    def editCompliment(self, idOfCompliment: int):
        connection = openDatabase("localhost", "root", "root", "db_ouvidoria")

        if idOfCompliment == 0 or idOfCompliment > len(self.complimentsIds):
            formatter.errorEmitter("Elogio não encontrado!")
        else:
            newCompliment = validate.readString("\nDigite seu novo elogio aqui:\n")
            id = self.complimentsIds[idOfCompliment - 1]
            sqlCode = "UPDATE feedbacks SET feedback = %s WHERE id = %s"
            data = (newCompliment, id)
            updateDatabase(connection, sqlCode, data)

            formatter.successEmitter("Elogio editado com sucesso!")

        closeDatabase(connection)
