class Mon:
    NAME = "Lili"

    def __init__(self):
        self.__introduce__()

    def __introduce__(self):
        print("Hi, My name is " + self.NAME + "!")


lucy = Mon()
print(lucy)
