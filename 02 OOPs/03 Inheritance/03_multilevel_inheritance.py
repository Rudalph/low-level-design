# A class inherits from a class, which itself inherits from another class.

class Grandparent:
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


child = Child()

child.house()  # From Grandparent
child.car()    # From Parent
child.bike()   # Child's own method