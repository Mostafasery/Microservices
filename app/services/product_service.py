class ProductService:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Smartphone"}
        ]

    def get_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        return next((product for product in self.products if product["id"] == product_id), None)
