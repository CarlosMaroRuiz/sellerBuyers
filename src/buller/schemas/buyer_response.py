from pydantic import BaseModel

class BuyerResponse(BaseModel):
    username: str
    message: str = "Buyer creado exitosamente"
    class Config:
        schema_extra = {
            "example": {
                "username": "Carlos",
                "message": "Buyer creado exitosamente"
            }
        }
