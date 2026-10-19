class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product
        return total
    
class InvoicePrinter:
    
    def __init__(self, cart):
        self.cart = cart

    def print_invoice(self):
        total = self.cart.calculate_total()
        print(f"Invoice: {total}")
        
class DatabaseSaver:
    
    def __init__(self, cart):
        self.cart = cart            

    def save_to_database(self):
        print("Saving shopping cart to database...")
        

user1_cart = ShoppingCart()
user1_cart.add_product(10)
user1_cart.add_product(20)
user1_cart.add_product(30)

user1_invoice_printer = InvoicePrinter(user1_cart)
user1_invoice_printer.print_invoice()

user1_database_saver = DatabaseSaver(user1_cart)
user1_database_saver.save_to_database()