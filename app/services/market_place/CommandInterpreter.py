import string
from app.services.market_place.models.MarketPlace import MarketPlace


class CommandInterpreter:
    @staticmethod
    def interpret_command(market_place: MarketPlace, command: string) -> None:
        parts = command.split()

        if not parts:
            return

        operation = parts[0].lower()

        command_handlers = {
            "start_market": CommandInterpreter.start_market,
            "create_user": CommandInterpreter.create_user,
            "create_product": CommandInterpreter.create_product,
            "get_user": CommandInterpreter.get_user,
            "get_product": CommandInterpreter.get_product,
            "add_to_cart": CommandInterpreter.add_to_cart,
            "get_cart": CommandInterpreter.get_cart,
            "checkout": CommandInterpreter.checkout,
            "get_order_history": CommandInterpreter.get_order_history
        }

        handler = command_handlers.get(operation, CommandInterpreter.invalid_command)
        handler(market_place, parts)

    @staticmethod
    def start_market(market_place: MarketPlace, parts: [string]) -> None:
        print("MarketPlace started.")

    @staticmethod
    def create_user(market_place: MarketPlace, parts: [string]) -> None:
        buyer_service = market_place.buyer_service
        buyer_id = int(parts[1])
        name = parts[2]
        email = parts[3]
        password = parts[4]
        buyer = buyer_service.create_user(buyer_id, name, email, password)

        if not buyer:
            return
        
        print(f"User with ID {buyer_id} created.")

    @staticmethod
    def create_product(market_place: MarketPlace, parts: [string])-> None:
        product_service = market_place.product_service
        product_id = int(parts[1])
        price = float(parts[2])
        name = parts[3]
        availability = int(parts[4])

        product = product_service.create_product(product_id, price, name, availability)

        if not product:
            return
        
        print(f"User with ID {product_id} created.")


    @staticmethod
    def get_user(market_place: MarketPlace, parts: [string]) -> None:
        buyer_service = market_place.buyer_service
        buyer_id = int(parts[1])
        buyer = buyer_service.get_buyer(buyer_id)

        if not buyer:
            return
        
        print(f"User details: {buyer.__dict__}")

    @staticmethod
    def get_product(market_place: MarketPlace, parts: [string]) -> None:
        product_service = market_place.product_service
        product_id = int(parts[1])
        product = product_service.delete_product(product_id)

        if not product:
            return
        
        print(f"Product with ID {product_id} deleted.")

    @staticmethod
    def add_to_cart(market_place: MarketPlace, parts: [string]) -> None:
        cart_service = market_place.cart_service
        buyer_id = int(parts[1])
        product_id = int(parts[2])
        quantity = int(parts[3])
        cart = cart_service.addToCart(market_place.buyer_service, market_place.product_service, buyer_id, product_id, quantity)

        if cart and len(cart) > 0:
            return
        
        print(f"Product with ID {product_id} added to cart for user {buyer_id}.")

    @staticmethod
    def get_cart(market_place: MarketPlace, parts: [string]) -> None:
        cart_service = market_place.cart_service
        buyer_id = int(parts[1])
        cart = cart_service.getCart(market_place.buyer_service, buyer_id)
        if not cart:
            return
        
        print(f"User {buyer_id}'s Cart:\n")
        for cart_item in cart:
            print(cart_item.__dict__)

    @staticmethod
    def checkout(market_place: MarketPlace, parts: [string]) -> None:
        buyer_service = market_place.buyer_service
        buyer_id = int(parts[1])
        shipping_address = parts[2]
        checkout = buyer_service.checkout(buyer_id, shipping_address)

        if not checkout:
            return
        
        print(f"Checkout completed for user {buyer_id}.")

    @staticmethod
    def get_order_history(market_place: MarketPlace, parts: [string]) -> None:
        buyer_service = market_place.buyer_service
        buyer_id = int(parts[1])
        order_history = buyer_service.get_order_history(buyer_id)
        print(f"User {buyer_id}'s Order History:")
        for order in order_history:
            print(order.__dict__)

    @staticmethod
    def invalid_command(market_place: MarketPlace, parts: [string]) -> None:
        print("Invalid command. Please check your command.")