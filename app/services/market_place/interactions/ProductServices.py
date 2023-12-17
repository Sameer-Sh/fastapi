import string
from app.services.market_place.models.Product import Product


class ProductServices:
    def __init__(self):
        self.products = {}

    def create_product(self, product_id: int, price: float, name: string, availability: int):
        # Assuming product_id is unique
        if product_id in self.products:
            print("Product with this ID already exists.")
            return
        
        new_product = Product(product_id, price, name, availability)
        self.products[product_id] = new_product

    def get_all_products(self):
        return list(self.products.values())

    def get_available_products(self):
        return [product for product in self.products.values() if product.availability > 0]

    def get_products_in_a_price_range(self, min_price: float, max_price: float):
        return [product for product in self.products.values() if min_price <= product.price <= max_price]

    def get_product_by_id(self, product_id: int) -> Product:
        if product_id not in self.products:
            print("Product with this ID does not exist.")
            return
        
        return self.products[product_id]
    
    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)

        if product:
            product.availability = 0
        
        return product