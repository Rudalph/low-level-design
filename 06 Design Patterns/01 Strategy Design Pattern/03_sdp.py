'''
Robot Workforce System
'''

from abc import ABC, abstractmethod

class Robot:
    def __init__(self, w, t, f):
        self.walk = w
        self.talk = t
        self.fly = f
        
    def projection(self):
        '''This is how the Robot will look'''
        pass
    

# Walking's abstract and concrete classes
class RobotWalk(ABC):
    @abstractmethod
    def walking(self):
        pass
    
class NormalWalk(RobotWalk):
    def walking(self):
        print('Normal Walk')

class HopWalk(RobotWalk):
    def walking(self):
        print('Hop Walk')
        
# Talking's abstract and concrete classes
class RobotTalk(ABC):
    @abstractmethod
    def talking(self):
        pass

class NormalTalk(RobotTalk):
    def talking(self):
        print('Normal Talk')

class SignTalk(RobotTalk):
    def talking(self):
        print('Sign Talk')
        
# Flying's abstract and concrete class
class RobotFly(ABC):
    @abstractmethod
    def flying(self):
        pass

class NormalFly(RobotFly):
    def flying(self):
        print('Normal Fly')

class JetFly(RobotFly):
    def flying(self):
        print('JetFly')
        
# Making different type of Robots
class CompanionRobot(Robot):
    def projection(self):
        print('Looks Like: Companion Robot')
        
# Companion Robot Specifications
# Walk Feature: Normal Walk
# Talk Feature: Normal Talk 
# Fly Feature: Normal Fly

w = NormalWalk()
t = NormalTalk()
f = NormalFly()

companion_robot_1 = CompanionRobot(w, t, f)
companion_robot_1.walk.walking()
companion_robot_1.talk.talking()
companion_robot_1.fly.flying()


'''
1. Strategy Interface: RobotWalk, RobotTalk, RobotFly
2. Concrete Strategies: NormalWalk, HopWalk, NormalTalk, etc.
3. Context Class: Robot
4. Composition: Passing w, t, f into Robot
5. Multiple interchangeable behaviors:	Walk, Talk, Fly
6. Runtime Strategy Switching:	Possible, Not Demonstrated
'''


'''
Better Approach

class Robot:
    def __init__(self, w, t, f):
        self.walk = w
        self.talk = t
        self.fly = f

    def perform_walk(self):
        self.walk.walking()

    def perform_talk(self):
        self.talk.talking()

    def perform_fly(self):
        self.fly.flying()

    def projection(self):
        pass
        

companion_robot_1 = CompanionRobot(
    NormalWalk(),
    NormalTalk(),
    NormalFly()
)

companion_robot_1.perform_walk()
companion_robot_1.perform_talk()
companion_robot_1.perform_fly()


# Runtime strategy switching

companion_robot_1 = CompanionRobot(
    NormalWalk(),
    NormalTalk(),
    NormalFly()
)

companion_robot_1.perform_walk()
# Normal Walk

# Change walking strategy at runtime
companion_robot_1.walk = HopWalk()

companion_robot_1.perform_walk()
# Hop Walk
'''

