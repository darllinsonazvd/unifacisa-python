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
            string = str(input(value))

            if string == "":
                print("\033[31mErro: Texto vazio, digite algo!\033[m")
            else:
                return string


class Formatter:
    def line(self, size=100):
        return "=" * size

    def header(self, value):
        print("-" * 100)
        print(value.center(100))
        print("-" * 100)

    def menu(self, list):
        count = 1

        for items in list:
            print(f"\033[33m{count})\033[m \033[34m{items}\033[m")
            count += 1

    def successEmitter(self, msg):
        print(f"\n\033[92m{msg}\033[m\n")

    def errorEmitter(self, err):
        print(f"\n\033[31mErro: {err}\033[m\n")
