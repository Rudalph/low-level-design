class Menu:
    def __init__(self):
        self.menu_items = {}
    
    def add_dishes(self, arr):
        for dish_price in arr:
            dish = dish_price[0]
            price = dish_price[1]
            self.menu_items[dish] = price
    
    def remove_dish(self, dish_name):
        if dish_name in self.menu_items:
            self.menu_items.pop(dish_name)
    
    def update_dish(self, dish_name, new_price):
        if dish_name in self.menu_items:
            self.menu_items[dish_name] = new_price