# Runtime polymorphism means that the behavior
#                   of a method is decided while program is running, based on the object calling it.

# Method Overriding a child class provides its own version of a method already defined in the parent class.


class Payment:
    def transaction_success(self):
        print("Payment Successful")

class ApplePay(Payment):
    def transaction_success(self):
        print("Payment Successful using ApplePay")

class GooglePay(Payment):
    def transaction_success(self):
        print("Payment Successful using GooglePay")

class CreditCard(Payment):
    def transaction_success(self):
        print("Payment Successful using Creditcard")

payment1 = ApplePay()
payment1.transaction_success()

payment_types = [ApplePay(), GooglePay(), CreditCard()]

for pay in payment_types:
    pay.transaction_success()

