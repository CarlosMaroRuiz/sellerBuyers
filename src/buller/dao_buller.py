from sqlalchemy.orm import Session

from src.buller.schemas.buller_schema import Buyer


class BuyerDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, buyer: Buyer):
        self.db.add(buyer)
        self.db.commit()
        self.db.refresh(buyer)
        return buyer