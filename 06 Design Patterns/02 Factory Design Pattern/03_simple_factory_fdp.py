'''Simple Factory'''

from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def prepare_burger(self):
        pass
    
class BasicBurger(Burger):
    def prepare_burger(self):
        print('Preparing Basic Burger')
        
class StandardBurger(Burger):
    def prepare_burger(self):
        print('Preparing Standard Burger')
        
class PremiumBurger(Burger):
    def prepare_burger(self):
        print('Preparing Premium Burger')
        
class BurgerFactory:
    def create_burger(self, type):
        if type == 'Basic':
            return BasicBurger()
        elif type == 'Standard':
            return StandardBurger()
        elif type == 'Premium':
            return PremiumBurger()
        else:
            return 0
        
burger_factory = BurgerFactory()
burger_prep = burger_factory.create_burger('Premium')
burger_prep.prepare_burger()
        
    