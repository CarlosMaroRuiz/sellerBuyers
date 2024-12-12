from sqlalchemy.orm import Session
from src.seller.schemas.seller_model import Seller

class seller_dao:
    def __init__(self, db: Session):
        self.db = db

    def create(self, seller: Seller):
        self.db.add(seller)
        self.db.commit()
        self.db.refresh(seller)
        return seller