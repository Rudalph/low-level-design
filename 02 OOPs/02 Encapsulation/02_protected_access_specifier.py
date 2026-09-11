class Employee:
    
    def __init__(self, name):
        self._name = name  # Protected attribute

e1 = Employee("John")
print(e1._name)  
# Output: John    
# Note: Although the attribute is protected, it can still be accessed outside the class.
# Unlike Java/C++, Python does not enforce protected access.
# The _variable convention means: "This is intended for internal/class/subclass use; don't access it directly unless necessary."
# Proper Example of Protected Access:
class Student:

    def __init__(self, name):
        self._name = name


class GraduateStudent(Student):

    def show_name(self):
        print(self._name)


student = GraduateStudent("Rudalph")
student.show_name()