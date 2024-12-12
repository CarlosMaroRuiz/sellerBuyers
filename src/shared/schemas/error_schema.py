from pydantic import BaseModel

class ErrorResponse(BaseModel):
    code_error: int
    msg: str

    class Config:
        schema_extra = {
            "example": {
                "code_error": 400,
                "msg": "Invalid request"
            }
        }
