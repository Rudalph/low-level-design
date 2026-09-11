# Polymorphism means one interface/method can behave differently depending on the object.
# There are 2 types of polymorphism in Python:
# 1. Compile-time polymorphism (Method Overloading)
# 2. Run-time polymorphism (Method Overriding)

# There is no method overlaoding in Python. 
# But we can achieve method overloading by using 
# 1. default arguments.
# 2. variable-length arguments (*args, **kwargs)

# Method Overloading using default arguments
class Calculator:
    def add(self, a, b = 0, c = 0):
        return a + b + c
    
calc = Calculator()
print(calc.add(5))          # Output: 5 (only one argument provided)    
print(calc.add(5, 10))      # Output: 15 (two arguments provided)
print(calc.add(5, 10, 15))  # Output: 30 (three arguments provided)

# Method Overloading using variable-length arguments *args
# args is stored as a tuple.
class Calculator:
    def add(self, *args):
        print("Arguments received:", args)  # Print the received arguments
        return sum(args)    
    
calc = Calculator()
print(calc.add(5))                 # Output: 5 (only one argument provided)
print(calc.add(5, 10))             # Output: 15 (two arguments provided)
print(calc.add(5, 10, 15))         # Output: 30 (three arguments provided)

# Method Overloading using variable-length arguments **kwargs
# kwargs is stored as a dictionary.
class Calculator:
    def add(self, **kwargs):
        print("Keyword arguments received:", kwargs)  # Print the received keyword arguments
        return sum(kwargs.values())     
    
calc = Calculator()
print(calc.add(a=5))                 # Output: 5 (only one keyword argument provided)
print(calc.add(a=5, b=10))           # Output: 15 (two keyword arguments provided)
print(calc.add(a=5, b=10, c=15))     # Output: 30 (three keyword arguments provided)
