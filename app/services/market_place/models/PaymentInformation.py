import string


class PaymentInformation:
    def __init__(self, total_bill: float, status: string):
        self.total_bill = total_bill
        self.status = status