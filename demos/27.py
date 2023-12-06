class Student:
    def __init__(self):
        return


lili = Student()

lili.gender = "\nfemale\n"

print(lili.gender)


def talk(content):
    print(content)


lili.__talk__ = talk
lili.__talk__("I‘m Lili !")
