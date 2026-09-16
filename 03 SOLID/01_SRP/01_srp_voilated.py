class ShoppingCart:
    
    def __init__(self):
        self.products = []
    
    # This function is Justified here 
    def add_product(self, product):
        self.products.append(product)
    
    # This function is Justified here    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product
        return total
    
    # This function voilates SRP
    def print_invoice(self):
        total = self.calculate_total()
        print(f"Invoice: {total}")
    
    # This function voilates SRP    
    def save_to_database(self):
        print("Saving shopping cart to database...")
        
user1 = ShoppingCart()
user1.add_product(10)
user1.add_product(20)
user1.add_product(30)

user1.print_invoice()

user1.save_to_database()
        