from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Precio del producto, debe ser mayor a 0.")
    stoke: int = Field(..., ge=0, description="Cantidad de stock disponible, no puede ser negativa.")

    class Config:
        orm_mode = True
