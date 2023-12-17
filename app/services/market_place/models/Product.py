import string


class Product:
    def __init__(self, product_id: int, price: float, name: string, availability: int):
        self. product_id = product_id
        self.price = price
        self.name = name
        self.availability = availability