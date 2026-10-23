'''
Question 3: E-Commerce Discount and Payment System (Medium)

You are developing an e-commerce checkout system that applies discounts and processes customer payments.

The system should perform the following tasks:
    1. Store order details (Order ID, customer name, and total amount).
    2. Apply discounts based on customer membership:
        - Regular Customer: 0% discount
        - Silver Customer: 5% discount
        - Gold Customer: 10% discount
    3. Calculate the final payable amount after applying the discount.
    4. Support the following payment methods:
        - Credit Card: Process payment using card details.
        - UPI: Process payment using a UPI ID.
        - PayPal: Process payment using an email address.
    5. Simulate payment processing by printing a successful payment message containing the payment method and final amount.
    6. The system should allow new discount types and payment methods to be added without modifying existing discount or payment processing logic.
Your Task: Implement the E-Commerce Checkout System using OOP while following OCP and SRP.

Demonstrate that you can extend the system with:
    - Platinum Customer: 15% discount
    - Bank Transfer: A new payment method using bank account details

Both extensions should work without modifying existing classes.
'''

from abc import ABC, abstractmethod

class OrderDetails:
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        
    def get_order_details(self):
        return {
            'order_id' : self.order_id,
            'customer_name' : self.customer_name,
            'total_amount' : self.total_amount
        }

class Discounts(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

class RegularCustomerDiscounts(Discounts):
    def __init__(self, order):
        self.order = order
    
    def calculate_discount(self):
        return (self.order.get_order_details()['total_amount'] * 0) / 100

class SilverCustomerDiscounts(Discounts):
    def __init__(self, order):
        self.order = order
    
    def calculate_discount(self):
        return (self.order.get_order_details()['total_amount'] * 5) / 100
    
class GoldCustomerDiscounts(Discounts):
    def __init__(self, order):
        self.order = order
    
    def calculate_discount(self):
        return (self.order.get_order_details()['total_amount'] * 10) / 100
    
class FinalPayableAmount:
    def __init__(self, order, customer_type):
        self.customer_type = customer_type
        self.order = order
    
    def payable_amount(self):
        amount = self.order.get_order_details()['total_amount'] - self.customer_type.calculate_discount()
        print(f'Final Payable Amount: {amount}')
        return amount
    
class PaymentMethods(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class CreditCard(PaymentMethods):
    def __init__(self, order, payable_amount):
        self.order_details = order.get_order_details()
        self.order_id = self.order_details['order_id']
        self.customer_name = self.order_details['customer_name']
        self.total_amount = self.order_details['total_amount']
        self.payable_amount = payable_amount.payable_amount()
        
    def pay(self):
        print(f'Order Id: {self.order_id}')
        print(f'Customer Name: {self.customer_name}')
        print(f'Total Amount: {self.total_amount}')
        print(f'Payable Amount: {self.payable_amount}')
        print(f'Payment Method: Credit Card')
        
class UPI(PaymentMethods):
    def __init__(self, order, payable_amount):
        self.order_details = order.get_order_details()
        self.order_id = self.order_details['order_id']
        self.customer_name = self.order_details['customer_name']
        self.total_amount = self.order_details['total_amount']
        self.payable_amount = payable_amount.payable_amount()
        
    def pay(self):
        print(f'Order Id: {self.order_id}')
        print(f'Customer Name: {self.customer_name}')
        print(f'Total Amount: {self.total_amount}')
        print(f'Payable Amount: {self.payable_amount}')
        print(f'Payment Method: UPI')

class PayPal(PaymentMethods):
    def __init__(self, order, payable_amount):
        self.order_details = order.get_order_details()
        self.order_id = self.order_details['order_id']
        self.customer_name = self.order_details['customer_name']
        self.total_amount = self.order_details['total_amount']
        self.payable_amount = payable_amount.payable_amount()
        
    def pay(self):
        print(f'Order Id: {self.order_id}')
        print(f'Customer Name: {self.customer_name}')
        print(f'Total Amount: {self.total_amount}')
        print(f'Payable Amount: {self.payable_amount}')
        print(f'Payment Method: PayPal')
    

'''In future we need to add Paltinum Customer Discount and Bank Transfer Payment Method'''

class PlatinumCustomerDiscounts(Discounts):
    def __init__(self, order):
        self.order = order
    
    def calculate_discount(self):
        return (self.order.get_order_details()['total_amount'] * 15) / 100
    
class BankTransfer(PaymentMethods):
    def __init__(self, order, payable_amount):
        self.order_details = order.get_order_details()
        self.order_id = self.order_details['order_id']
        self.customer_name = self.order_details['customer_name']
        self.total_amount = self.order_details['total_amount']
        self.payable_amount = payable_amount.payable_amount()
        
    def pay(self):
        print(f'Order Id: {self.order_id}')
        print(f'Customer Name: {self.customer_name}')
        print(f'Total Amount: {self.total_amount}')
        print(f'Payable Amount: {self.payable_amount}')
        print(f'Payment Method: Bank Transfer')

order = OrderDetails(1, 'Rudalph Gonsalves', 5000)
regular_customer = RegularCustomerDiscounts(order)
payable_amount = FinalPayableAmount(order, regular_customer)
credit_card_payment = CreditCard(order, payable_amount)
credit_card_payment.pay()

