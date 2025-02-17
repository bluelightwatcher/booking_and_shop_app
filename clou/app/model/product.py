from app.model.base_model import BaseModel 
import re

class Product(BaseModel):
    def __init__(self,description, price, qty):
        super().__init__()
        self.description = self.description_check(description)
        self.price = self.price_check(price)
        self.qty = self.qty_check(qty)

    @staticmethod
    def description_check(description):

        if not isinstance(description, str):
            raise TypeError("la description doit etre en lettres")

        elif 0< len(description) >151:
            raise ValueError("la description doit etre entre 0 et 150 characteres")

        return description

    @staticmethod
    def price_check(price):

        if price < 0:
            raise ValueError("le prix doit être supérieur à zéro")

        elif isinstance(price, str):
            raise TypeError("le prix doit être en chiffres")

        return price

    @staticmethod
    def qty_check(qty):

        if qty < 0:
            raise ValueError("la quantité doit être supérieure à zéro")

        elif isinstance(qty, str):
            raise TypeError("la quantité doit être en chiffres")

        return  qty
