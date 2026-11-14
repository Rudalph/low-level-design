from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_price(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass

class BasicCoffee(Coffee):
    def get_price(self):
        return 10
    
    def get_description(self):
        return 'Milk, Water, Cofee Powder, Sugar'
    
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_price(self):
        return self.coffee.get_price()
    
    def get_description(self):
        return self.coffee.get_description()
    
class MilkCoffeeDecorator(CoffeeDecorator):
    def get_price(self):
        return self.coffee.get_price() + 10
    
    def get_description(self):
        return self.coffee.get_description() + ' + Milk Powder'
    
class ChocolateCoffeeDecorator(CoffeeDecorator):
    def get_price(self):
        return self.coffee.get_price() + 20
    
    def get_description(self):
        return self.coffee.get_description() + ' + Chocolate'

# order basic coffee
coffee = BasicCoffee()

# Add milk
milk_coffee = MilkCoffeeDecorator(coffee)

# add chocolate
chocolate_coffee = ChocolateCoffeeDecorator(milk_coffee)

'''or'''

coffee = ChocolateCoffeeDecorator(MilkCoffeeDecorator(BasicCoffee()))
print(coffee.get_description())
print(coffee.get_price())