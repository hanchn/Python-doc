class Student(object):
    __slots__ = ("name", "age")

    def __init__(self):
        return


girl = Student()

girl.name = "lili"
print("My name is", girl.name, "!")
girl.gender = "female"
print(girl.gender)
