from domains.claims import *
from domains.ideas import *
from domains.compliments import *
from utils import *
from db.databaseOperations import *

validate = Validator()
formatter = Formatter()

claims = Claims()
ideas = Ideas()
compliments = Compliments()

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
        claims.getClaims()
        ideas.getIdeas()
        compliments.getCompliments()
    elif option == 2:  # Add feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Elogio"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            claim = validate.readString("\nDigite sua reclamação:\n")
            claims.addClaim(username, claim)
        elif category == 2:
            idea = validate.readString("\nDigite sua ideia:\n")
            ideas.addIdea(username, idea)
        elif category == 3:
            other = validate.readString("\nDigite seu elogio:\n")
            compliments.addCompliment(username, other)
        else:
            formatter.errorEmitter("Categoria não encontrada!")
    elif option == 3:  # Remove feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Elogio"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            print("\nQual a reclamação que você deseja remover?\n")
            claims.deleteClaim()
        elif category == 2:
            print("\nQual a ideia que você deseja remover?\n")
            ideas.deleteIdea()
        elif category == 3:
            print("\nQual o elogio que você deseja remover?\n")
            compliments.deleteCompliment()
    elif option == 4:  # Edit feedbacks
        formatter.header("Categorias:")
        formatter.menu(["Reclamação", "Ideia", "Elogio"])

        category = validate.readInt("\nQual a categoria do seu feedback? (1 / 2 / 3) ")

        if category == 1:
            print("\nQual a reclamação que você deseja editar?\n")

            claims.getClaims()

            idOfClaim = validate.readInt("\nNúmero da reclamação: ")

            claims.editClaim(idOfClaim)
        elif category == 2:
            print("\nQual a ideia que você deseja editar?\n")

            ideas.getIdeas()

            idOfIdea = validate.readInt("\nNúmero da ideia: ")

            ideas.editIdea(idOfIdea)
        elif category == 3:
            print("\nQual o elogio que você deseja editar?\n")

            compliments.getCompliments()

            idOfCompliment = validate.readInt("\nNúmero do elogio: ")

            compliments.editCompliment(idOfCompliment)
    elif option == 5:  # Quit
        closeDatabase(connection)
        formatter.header("Obrigado por utilizar o sistema de ouvidoria da Unifacisa!")
        print()
        print("Darllinson Azevedo | 2022".center(100))
        print("https://www.github.com/darllinsonazvd".center(100))
        print()
        break
    else:  # Error handling
        formatter.errorEmitter("Opção inválida!")
