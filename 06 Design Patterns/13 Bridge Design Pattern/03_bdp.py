from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, engine):
        self.engine = engine
    
    @abstractmethod    
    def drive(self):
        pass
    
class SUV(Car):
    def drive(self):
        self.engine.start_engine()
        print('Driving SUV Car')

class Sedan(Car):
    def drive(self):
        self.engine.start_engine()
        print('Driving Sedan Car')
        
class Engine(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class PetrolEngine(Engine):
    def start_engine(self):
        print('Starting Petrol Engine')

class ElectricEngine(Engine):
    def start_engine(self):
        print('Starting Electric Engine')
        
class CNGEngine(Engine):
    def start_engine(self):
        print('Starting CNG Engine')

scoripo_engine = PetrolEngine()
scorpio = SUV(scoripo_engine)
scorpio.drive()