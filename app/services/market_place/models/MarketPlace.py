from app.services.market_place.interactions.BuyerServices import BuyerServices
from app.services.market_place.interactions.CartServices import CartServices
from app.services.market_place.interactions.ProductServices import ProductServices


class MarketPlace:
    def __init__(self,buyer_service: BuyerServices, product_service: ProductServices, cart_service: CartServices):
        self.buyer_service = buyer_service
        self.product_service = product_service
        self.cart_service = cart_service