from sqlalchemy import Column, Integer, String
from src.db.models.base import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    __tablename__ = "Rol"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String(45), nullable=False)

    users = relationship("User", back_populates="rol")
