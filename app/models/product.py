class Product:

    type: str
    user_id: int
    product_code: str
    purchase_price: float
    product_description: str

    def to_dict(self):
        return self.__dict__
