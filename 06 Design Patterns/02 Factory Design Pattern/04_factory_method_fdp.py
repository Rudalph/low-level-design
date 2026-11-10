'''Factory Method'''

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
        
class HardBurger(Burger):
    def prepare_burger(self):
        print('Preparing Hard Burger')

class SoftBurger(Burger):
    def prepare_burger(self):
        print('Preparing Soft Burger')

class BurgerFactory(ABC):
    @abstractmethod
    def create_burger_object(self, type):
        pass

class SingBurgerFactory(BurgerFactory):
    def create_burger_object(self, type):
        if type == 'Basic':
            return BasicBurger()
        elif type == 'Standard':
            return StandardBurger()
        elif type == 'Premium':
            return PremiumBurger()
        else:
            return 0

class KingBurgerFactory(BurgerFactory):
    def create_burger_object(self, type):
        if type == 'Hard':
            return HardBurger()
        elif type == 'Soft':
            return SoftBurger()
            


sing_burger_factory = SingBurgerFactory()
burger_creator_1 = sing_burger_factory.create_burger_object('Premium')
burger_creator_1.prepare_burger()

king_burger_factory = KingBurgerFactory()
burger_creator_2 = king_burger_factory.create_burger_object('Hard')
burger_creator_2.prepare_burger()
        