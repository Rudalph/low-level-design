# We have 3 access modifiers in Python:
# 1. Public: Members (attributes and methods) are accessible from anywhere. 
# 2. Protected: Members are accessible within the class and its subclasses.
# 3. Private: Members are accessible only within the class.

class Student:
    
    def __init__(self, name):
        self.name = name  # Public attribute
        
s1 = Student("Rudalph")
print(s1.name)  # Output: Rudolph



# Note:
# Python doesn't have true access modifiers like Java's private, protected, and public.
# Instead, Python uses naming conventions and name mangling:
# name       → Public
# _name      → Protected convention
# __name     → Private via name mangling

'''Python doesn't enforce traditional access specifiers like Java. 
It uses naming conventions for public/protected members and name mangling for private members.'''
