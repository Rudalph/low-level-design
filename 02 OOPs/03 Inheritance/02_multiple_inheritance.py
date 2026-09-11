# Multiple Inheritance
# One child class inherits from multiple parent classes.

class Father:
    def work(self):
        print("Father works")
    
    def show(self):
        print("Father's show")


class Mother:
    def cook(self):
        print("Mother cooks")
    
    def show(self):
        print("Mother's show")


class Child(Father, Mother):
    pass


child = Child()

child.work()   # From Father
child.cook()   # From Mother

# Multiple inheritance + same method → MRO determines which implementation Python uses
child.show()   # From Father (MRO: Child → Father → Mother → object)
print(Child.__mro__)  # Output: (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)