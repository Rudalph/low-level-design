from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    
# Class Dog inherits from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"  
    
# Class Cat inherits from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
# Create instances of Dog and Cat
dog = Dog()     
cat = Cat()

# Call the make_sound method for each instance
print(dog.make_sound())  # Output: Woof!    
print(cat.make_sound())  # Output: Meow!

# Attempting to create an instance of the abstract class Animal will raise an error
# animal = Animal()  # This will raise TypeError: Can't instantiate abstract class Animal with abstract methods make_sound

    