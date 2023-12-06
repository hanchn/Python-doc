class Mon:
    def __init__(self):
        return

    def __talk__(self, name):
        print("Hi, My name is " + name + "!")


class Baby(Mon):
    def __init__(self, name):
        super().__init__()
        self.__talk__(name)

    def __talk__(self, name):
        print("Hi, My name is " + name + "!")
        print("I’m a Baby!")


myBaby = Baby("Longlong")
