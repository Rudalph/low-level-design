''' Problem '''
class Database1:
    def __init__(self):
        print('Database1 Connected')
db1_1 = Database1()
db1_2 = Database1()
print(db1_1 is db1_2)

print('\n ----------------------------------------------------- \n')

''' Basic Solution - 1 '''
class Database2:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            print('Creating the 1st Instance')
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print('Instance Already Created')
            return cls.__instance
    
    def __init__(self):
        print('Database2 Connected')

db2_1 = Database2()
db2_2 = Database2()
print(db2_1 is db2_2)

# __new__ is dunder method which is responsible to create objects
# __init__ is dunder method used to initilize the objects
# in __init__ we use self to handle similarly we use cls in __new__ to handle class
# cls represent that class itself (Database2 class in our case)

# Every class by default inherits Object class
# So for creating object we use __new__ method of parent class using super keyword.

# We can use public, private or protected variable for instance storing

# Above code is not thread safe


print('\n ----------------------------------------------------- \n')

''' Solution 3 - Thread Safety '''

# Two threads can simultaneously check if instance is created or not and end up creating 2 objects

# What is critical section
# - A portion of code that accessess or modofies shared shared resources and must not be executed by
# multiple threads simultaneously

'''In our example critical section is
if cls.__instance is None:
    cls.__instance = super().__new__(cls)
'''

# What is locking?
# Locking ensures that only one thread can execute a critical section at a time

# What is thread safety?
# The code should behave as expected even when multiple thread are accessing at the same time

import threading

class Database3:
    __instance = None
    __lock = threading.Lock()
    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                print('Creating 1st Instance')
                cls.__instance = super().__new__(cls)
                return cls.__instance
            else:
                print('Instance Already Created')
                return cls.__instance
    
    def __init__(self):
        print('Database3 Connected')

db3_1 = Database3()
db3_2 = Database3()
print(db3_1 is db3_2)

# Locking is very expensive computationally

# Whar are we doing:
# Whenever a thread comes we are putting a lock
# What if we check if instance is not created only then put a lock?
# It is not right
'''
if __instance is None:
    with __lock:
        code to create instance
'''
# Whats going wrong?
# - Thread one T1 comes and check instance is not created enters the next line locks the criical section
# and starts working on creating thread but is in the process on creating instance and not yet created

# - Thread two T2 comes at the same time and checks and founds instance is not yet created (as T1 is still in the process of creating instance)
# but lock is applied by T1 so it waits at that line of code
# as soon as lock is finished it directly enters into the code of creating instance.

# Thus T1 and T2 end up creating 2 instances

# What is the Solution?
''' Double Checked Locking '''
'''
if __instance is None:
    with __lock:
        if __instance is None:
                code to create instance
'''

# 1st Lock: Avoid unnecessary locking if instance is already created and reduce computation of locking

# 2nd Lock: Ensure another thread hasn't created the instance while this thread was waiting for the lock


print('\n -----------------------FINAL------------------------------ \n')

class Database4:
    __instance = None
    __lock = threading.Lock()
    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    print('Creating 1st Instance')
                    cls.__instance = super().__new__(cls)
                    return cls.__instance
                else:
                    print('Instance Already Created By Some Other Thread')
                    return cls.__instance
        else:
            print('Instance Already Created')
            return cls.__instance
        
    def __init__(self):
        print('Database4 Connected')

db4_1 = Database4()
db4_2 = Database4()
print(db4_1 is db4_2)



print('\n -----------------------Early Initilization------------------------------ \n')

''' Different Approach for Singelton  Design Pattern '''
# Early Initilization
class A:
    def __init__(self):
        print('Class A Initilized')

_instance = A()

class Singelton:
    def get_classA_instance(self):
        return _instance

obj1 = Singelton().get_classA_instance()
obj2 = Singelton().get_classA_instance()

print(obj1 is obj2)

# Early initilization means creating the instance of the class immedialely when the class us loaded/defined
# rather than waiting for someone to req for the object
# Main difference between Early initilization and Lazy Initilization is:
# In Early initilization resources may be wasted if never used
# And in lazy initilization resources are used only when needed