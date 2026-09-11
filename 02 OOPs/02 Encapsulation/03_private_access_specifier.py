class Student:

    def __init__(self, name):
        self.__name = name


student = Student("Rudalph")

# print(student.__name)  # This will raise an AttributeError

# Python uses name mangling for __name
# Internally, it becomes approximately:_Student__name
print(student._Student__name)
# would work, but this should not be used as a normal way to access the private attribute.