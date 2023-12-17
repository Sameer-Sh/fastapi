import datetime
import string

from app.services.market_place.models.Buyer import Buyer
from app.services.market_place.models.Order import Order
from app.services.market_place.models.PaymentInformation import PaymentInformation


class BuyerServices:
    def __init__(self):
        self.buyers = {}

    def create_user(self,buyer_id: int, name: string, email: string, password: string):
        # Assuming buyer_id is unique
        if buyer_id in self.buyers:
            print("User with this ID already exists.")
            return

        new_buyer = Buyer(buyer_id, name, email, password, [], [], "active", True)
        self.buyers[buyer_id] = new_buyer

        return new_buyer

    def login_user(self, buyer_id: int):
        if buyer_id in self.buyers:
            print("User with this ID already exists.")
            return
        
        buyer = self.buyers[buyer_id]

        if buyer.is_logged_in:
            print("Already Logged In!!")

        buyer.status = 'active'

    def get_buyer(self, buyer_id: int):
        if buyer_id not in self.buyers:
            print("User with this ID does not exist.")
            return False

        return self.buyers[buyer_id]

    def get_order_history(self, buyer_id: int) -> [Order]:
        buyer = self.get_buyer(buyer_id)
        return buyer.Orders
    
    def get_all_users(self) -> [Buyer]:
        return list(self.buyers.values())
    
    def checkout(self, buyer_id: int, shipping_address: string):
        buyer = self.get_buyer(buyer_id)

        if not buyer:
            return False

        if len(buyer.Cart) == 0:
            print("Cart is empty. Cannot complete the checkout.")
            return False

        total_bill = sum(item.product.price * item.quantity for item in buyer.Cart)

        payment_info = PaymentInformation(total_bill, "Paid")

        order = Order(buyer_id, buyer.Cart, shipping_address, payment_info, "Completed", datetime.datetime.now())
        buyer.Orders.append(order)

        buyer.Cart = []

        return True