from app.services.market_place.models.CartItem import CartItem
from app.services.market_place.interactions.ProductServices import ProductServices
from app.services.market_place.interactions.BuyerServices import BuyerServices


class CartServices:
    def addToCart(self, buyer_service: BuyerServices, product_service: ProductServices, buyer_id: int, product_id: int, quantity: int):
        buyer = buyer_service.get_buyer(buyer_id)

        if not buyer:
            return

        if not buyer.is_logged_in:
            print("Please Login to Continue")
            return
        
        product = product_service.get_product_by_id(product_id)

        if not product:
            return

        if product.availability <= 0:
            print("Product is out of Stock!!")
            return

        # Check if the product is already in the cart
        existing_cart_item = next((item for item in buyer.Cart if item.product_id == product.product_id), None)

        if existing_cart_item:
            # Update the quantity if the product is already in the cart
            existing_cart_item.quantity += quantity
        else:
            # Add a new CartItem to the cart
            cart_item = CartItem(product, quantity)
            buyer.Cart.append(cart_item)
        
        product.availability = product.availability - 1

        return buyer.Cart

    def getCart(self,buyer_service: BuyerServices, buyer_id: int) -> [CartItem]:
        buyer = buyer_service.get_buyer(buyer_id)

        return buyer.Cart if buyer else None