"""
Definition: Software entities (classes modules, functions) should be open for extension but closed for modification

Simple terms:
 - open for extension = You can add new features easily
 - Closed for modification = Don't change existing working code

Example: adding new payment methods (Credit Card, UPI, PayPal) without modifying the existing payment processing code.

"""

############## BAD EXAMPLE #################

# class PaymentProcessor:
#     def pay(self,payment_method: str, amount: int):
#         if payment_method == 'UPI':
#             print()
#             print()
#         elif payment_method == 'credit_card':
#             print()
#             print()
#         elif payment_method == 'net_banking':
#             print()
#             print()

# payment_processor_obj = PaymentProcessor()
# payment_processor_obj.pay("credit_card",500)
# to add one more payment method we requier modification of one more elif statement which is a violation of open-closed principle

########## GOOD EXAMPLE ##############
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount:int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through UPI of Rs. {amount}")

class DebitCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through Debit card of Rs. {amount}")

class CreditCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through credit card of Rs. {amount}")

# new extension of paypal payment method

class PaypalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying through paypal method of Rs. {amount}")

class PaymentProcessor:
    def process_payment(self,payment_method: PaymentMethod,amount:int):
        payment_method.pay(amount)


debit = DebitCardPayment()
credit = CreditCardPayment()
paypal = PaypalPayment()

payment_processor = PaymentProcessor()

payment_processor.process_payment(debit,500)
payment_processor.process_payment(paypal,1000)


# now i can add easily paypal payment method without modifying anything it will just be an extension