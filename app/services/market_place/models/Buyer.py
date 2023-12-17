import string
from app.services.market_place.models.CartItem import CartItem
from app.services.market_place.models.Order import Order


class Buyer:
    def __init__(self, buyer_id: int, name: string, email: string, password: string, cart: [CartItem], orders: [Order], status: string, is_logged_in):
        self.buyer_id = buyer_id
        self.name = name
        self.email = email
        self.password = password
        self.Cart = cart
        self.Orders = orders
        self.status = status
        self.is_logged_in = is_logged_in