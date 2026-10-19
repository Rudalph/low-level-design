class Stripe:
    def stripe_payment(self, amount):
        print(f"Paid {amount} via stripe payment service")
        
class OrderService:
    def checkout(self, amount):
        stripe = Stripe()
        stripe.stripe_payment(amount)
        
order = OrderService()
order.checkout(100)

# OrderService is High Level Module
# Stripe is Low Level Module
# OrderService knows too much about Stripe
# If I update Stripe then OrderService might also need to be updated
        
    