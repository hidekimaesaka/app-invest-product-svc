from app.database import MongoDBConnection
from app.models.product import Product


class ProductRepository:
    def __init__(self):
        self.collection_name = "product"

    def create(self, product: Product):
        with MongoDBConnection() as db:
            result = db[self.collection_name].insert_one(product.to_dict())
            return result.inserted_id

    def find_all(self):
        with MongoDBConnection() as db:
            products = db[self.collection_name].find()
            return products
