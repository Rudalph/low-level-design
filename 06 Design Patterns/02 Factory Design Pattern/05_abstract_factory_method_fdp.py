'''Abstract Factory Method'''

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


class Pizza(ABC):
    @abstractmethod
    def prepare_pizza(self):
        pass

class SmallPizza(Pizza):
    def prepare_pizza(self):
        print('Preparing Small Size Pizza')

class MediumPizza(Pizza):
    def prepare_pizza(self):
        print('Preparing Medium Size Pizza')

class LargePizza(Pizza):
    def prepare_pizza(self):
        print('Preparing Large Size Pizza')

class AlphaPizza(Pizza):
    def prepare_pizza(self):
        print('Preparing Aplha Pizza')

class BravoPizza(Pizza):
    def prepare_pizza(self):
        print('Preparing Bravo Pizza')


class MealFactory(ABC):
    @abstractmethod
    def create_burger_object(self, type):
        pass
    
    @abstractmethod
    def create_pizza_object(self, type):
        pass

class SingFactory(MealFactory):
    def create_burger_object(self, type):
        if type == 'Basic':
            return BasicBurger()
        elif type == 'Standard':
            return StandardBurger()
        elif type == 'Premium':
            return PremiumBurger()
        else:
            return 0
    
    def create_pizza_object(self, type):
        if type == 'Small':
            return SmallPizza()
        elif type == 'Medium':
            return MediumPizza()
        elif type == 'Large':
            return LargePizza()
        else:
            return 0

class KingFactory(MealFactory):
    def create_burger_object(self, type):
        if type == 'Hard':
            return HardBurger()
        elif type == 'Soft':
            return SoftBurger()
        return 0
    
    def create_pizza_object(self, type):
        if type == 'Alpha':
            return AlphaPizza()
        elif type == 'Bravo':
            return BravoPizza()
        else:
            return 0
        
            


sing_factory = SingFactory()
sing_burger_creator = sing_factory.create_burger_object('Premium')
sing_burger_creator.prepare_burger()

king_factory = KingFactory()
king_pizza_creator = king_factory.create_pizza_object('Bravo')
king_pizza_creator.prepare_pizza()
        