# Types of inheritance: 
# Single, Multiple, Multilevel, Hierarchical, Hybrid
# Modes of Inheritance: (in C++ and Java)
# 1. Public Inheritance: Public members of the base class become public members of the derived class.
# 2. Protected Inheritance: Public and protected members of the base class become protected members of the derived class.
# 3. Private Inheritance: Public and protected members of the base class become private members of the derived class.
# Note: Private memebers of the base class are never inherited by the derived class.


# SINGLE INHERITANCE
# One child class inherits from one parent class.
class Animal:              # Parent
    def eat(self):
        print("Eating")


class Dog(Animal):         # Child
    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()                  # Inherited from Animal
dog.bark()                 # Dog's own method
