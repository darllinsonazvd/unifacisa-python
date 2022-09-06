class Validator:
    def readInt(self, value):
        while True:
            try:
                number = int(input(value))
            except (ValueError, TypeError):
                print("\033[31mErro: Insira um número inteiro!\033[m")
            else:
                return number

    def readString(self, value):
        while True:
            try:
                string = str(input(value))
            except (ValueError, TypeError):
                print("\033{31mErro: Insira um texto válido!\033[m")
            else:
                return string


class Formatter:
    def line(self, size=75):
        return "=" * size

    def header(self, value):
        print("-" * 75)
        print(value.center(75))
        print("-" * 75)

    def menu(self, list):
        count = 1

        for items in list:
            print(f"\033[33m{count})\033[m \033[34m{items}\033[m")
            count += 1
