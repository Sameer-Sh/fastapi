import datetime
import string
from app.services.market_place.models.CartItem import CartItem
from app.services.market_place.models.PaymentInformation import PaymentInformation


class Order:
    def __init__(self, buyer_id: int, cart : [CartItem], shipping_address: string, payment_information: PaymentInformation, status: string, order_date: datetime):
        self.buyer_id = buyer_id
        self.cart = cart
        self.shipping_address = shipping_address
        self.payment_information = payment_information
        self.status = status
        self.order_date = order_date