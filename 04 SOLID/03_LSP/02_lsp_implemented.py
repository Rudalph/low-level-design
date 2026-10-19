class Bird:
    def eat(self):
        print("Eating")
        
class FlyingBird(Bird):
    def fly(self):
        print("Flying")
        
class WalkingBirds(Bird):
    def walk(self):
        print("Walking")
        
# Here both the child classes can easily replace parent class
# There is no reason for code to break in any case