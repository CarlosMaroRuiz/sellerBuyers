from pydantic import BaseModel
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stoke: int
    idUser: int

    class Config:
        orm_mode = True
