from pydantic import BaseModel

class Seller_response(BaseModel):
    username: str
    message: str = "seller creado exitosamente"
    class Config:
        schema_extra = {
            "example": {
                "username": "Carlos",
                "message": "seller creado exitosamente"
            }
        }
