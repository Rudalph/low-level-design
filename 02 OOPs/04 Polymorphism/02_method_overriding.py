# Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()