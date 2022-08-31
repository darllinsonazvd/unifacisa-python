class1 = input()
class2 = input()
class3 = input()

if class1 == "vertebrado":
    if class2 == "ave":
        if class3 == "carnivoro":
            print("aguia")
        elif class3 == "onivoro":
            print("pomba")
    elif class2 == "mamifero":
        if class3 == "onivoro":
            print("homem")
        elif class3 == "herbivoro":
            print("vaca")
elif class1 == "invertebrado":
    if class2 == "inseto":
        if class3 == "hematofago":
            print("pulga")
        elif class3 == "herbivoro":
            print("lagarta")
    elif class2 == "anelideo":
        if class3 == "hematofago":
            print("sanguessuga")
        elif class3 == "onivoro":
            print("minhoca")
