from abc import ABC, abstractmethod

class PaymentProcessor:
    @abstractmethod
    def pay(self):
        pass
    
class Stripe(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via Stripe Payment Service")
        
class Paypal(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via Paypal Payment Sercice")
        
class OrderService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor
        
    def checkout(self, amount):
        self.payment_processor.pay(amount)

paymentOption = input("Enter payment option Stripe or Paypal")

if paymentOption == "Stripe":
    stripe = Stripe()
    order = OrderService(stripe)
    order.checkout(100)
else:
    paypal = Paypal()
    order = OrderService(paypal)
    order.checkout(200)