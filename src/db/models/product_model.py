from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.db.models.base import Base


class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    stoke = Column(Integer, nullable=False)
    idUser = Column(Integer, ForeignKey("User.id"), nullable=False)

    user = relationship("User", back_populates="products")


