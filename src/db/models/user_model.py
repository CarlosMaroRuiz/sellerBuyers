from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.models.base import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    idRol = Column(Integer, ForeignKey("Rol.id"), nullable=False)
    rol = relationship("Rol", back_populates="users")

    products = relationship("Product", back_populates="user")
