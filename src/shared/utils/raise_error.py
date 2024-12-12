from fastapi import HTTPException
from src.shared.schemas.error_schema import ErrorResponse

def raise_error(status_code: int, code_error: int, msg: str):
    error_response = ErrorResponse(code_error=code_error, msg=msg)
    raise HTTPException(
        status_code=status_code,
        detail=error_response.dict()
    )
