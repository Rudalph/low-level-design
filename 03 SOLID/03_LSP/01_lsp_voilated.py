# We have a class bird and it can eat and fly
class Bird:
    def eat(self):
        print("Eating")
        
    def fly(self):
        print("Flying")
        
class Sparrow:
    def sparrow_colour(self):
        print("Green")
        
# Now we have a class penguin that is child class of bird
# But Penguins can't fly
class Penguin(Bird):
    # It will automatically have the property of eating
    # But we need to update the flying method
    
    def fly(self):
        raise Exception("Penguins can't fly")

# Here is voilation of Liskov Substitution Principal
# LSP says parent should be replacable by child
# But if we call parent's fly method it will say "Flying"
# And if we call child's fly method it will raise exception 

# parent class Bird promised: bird.fly() would work
# But Penguin cannot fulfill that expectation.