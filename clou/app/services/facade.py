from app.persistence.repository import InMemoryRepository
from app.model.user import User
from app.model.product import Product

class ClouFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.product_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User operations go here 
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Product operations go here
    def create_product(self, product_data):
        product = Product(**product_data)
        self.product_repo.add(product)
        return product

    def get_product(self, product_id):
        return self.product_repo.get(product_id)


    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

facade = ClouFacade()
