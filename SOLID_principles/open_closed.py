#rossz példa
#class Invoice:
#    def __init__(self, payment_type):
#        self.payment_type = payment_type
#
#   def process_payment(self):
#        if self.payment_type == "credit_card":
#           print("Bankkártya")
#        elif self.payment_type == "paypal":
#           print("Paypal")

class PaymentProcessor:
    def process(self):
        raise NotImplementedError()

class CreditCardPayment(PaymentProcessor):
    def process(self):
        print("Credit Card Payment")

class Paypal(PaymentProcessor):
    def process(self):
        print("Paypal")

class Invoice:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_payment(self):
        self.payment_processor.process()