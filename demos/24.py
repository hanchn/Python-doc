class Mon:
    NAME = "Lili"

    def __init__(self):
        return

    def __introduce__(self, name):
        print("Hi, My name is " + (self.NAME, name)[name != self.NAME] + "!")


lucy = Mon()
lucy.__introduce__("Lucy")
