'''
Question 2: Online Shopping Order System

You are building a basic order management system for an online shopping website.

The system should perform the following tasks:
    1. Store customer details (name and email).
    2. Store ordered products with their names, prices, and quantities.
    3. Calculate the total order amount.
    4. Apply a 10% discount if the total exceeds ₹5,000.
    5. Generate an order invoice containing customer details, products, and final amount.
    6. Save the invoice to a .txt file.

Your Task: Design the system using classes so that each class has a clear and separate responsibility.
'''

class CustomerDetails:
    def __init__(self, name, email):
        self.customer_name = name
        self.customer_email = email
    
    def get_customer_details(self):
        return {'customer_name':self.customer_name, 'customer_email':self.customer_email}
    
class ProductDetails:
    def __init__(self, customer):
        self.customer = customer
        self.product_names = []
        self.product_prices = []
        self.product_quantaties = []
    
    def add_product(self, product_name, product_price, product_quantity):
        self.product_names.append(product_name)
        self.product_prices.append(product_price)
        self.product_quantaties.append(product_quantity)
        
    def display_cart(self):
        print('===Displaying Card===')
        print(f"Product Names: {self.product_names}")
        print(f"Product Prices: {self.product_prices}")
        print(f"Product Quantaties: {self.product_quantaties}")

    def get_product_details(self):
        return {
                'product_names':self.product_names, 
                'product_prices':self.product_prices, 
                'product_quantaties':self.product_quantaties
               }
        
class OrderAmount:
    def __init__(self, product_details_executer):
        self.product_details_executer = product_details_executer
        
    def get_discount(self, amount):
        return (amount * 10)/100
    
    def calculate_amount(self):
        product_prices = self.product_details_executer.get_product_details()['product_prices']
        product_quantaties = self.product_details_executer.get_product_details()['product_quantaties']
        
        total = 0
        for price, quantity in zip(product_prices, product_quantaties):
            total = total + (price*quantity)
        
        if total > 5000:
            total = total - self.get_discount(total)
        
        return total
    
class GenerateInvoice:
    def __init__(self, product_details_executer, amount_extractor):
        self.product_details_executer = product_details_executer
        self.amount_extractor = amount_extractor
    
    def generate_invoice(self):
        product_names = self.product_details_executer.get_product_details()['product_names']
        product_prices = self.product_details_executer.get_product_details()['product_prices']
        product_quantaties = self.product_details_executer.get_product_details()['product_quantaties']
        total = self.amount_extractor.calculate_amount()
        
        print(f"Name \t Price \t Quantity \t Amount")
        for name, price, quantity in zip(product_names, product_prices, product_quantaties):
            print(f'{name} \t {price} \t {quantity} \t {price*quantity}')
        print(f'Total Amount: {total}')
        
class SaveInvoice:
    def __init__(self, invoice_generator):
        self.invoice_generator = invoice_generator
        
    def save_invoice(self):
        print('===Generating and Saving Invoice to DB===')
        self.invoice_generator.generate_invoice()
        print(f"Saved to Database")
            

customer = CustomerDetails("Rudalph", 'gonsalvesrudalph2003@gmail.com')

product_details_executer = ProductDetails(customer)
product_details_executer.add_product('oil', 100, 2)
product_details_executer.add_product('brush', 50, 3)
product_details_executer.display_cart()

amount_extractor = OrderAmount(product_details_executer)
print(amount_extractor.calculate_amount())

invoice_generator = GenerateInvoice(product_details_executer, amount_extractor)
invoice_generator.generate_invoice()

invoice_saver = SaveInvoice(invoice_generator)
invoice_saver.save_invoice()