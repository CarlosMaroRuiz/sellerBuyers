from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from src.config import  Config
from src.shared.utils.custom_exeption import CustomAppException

config = Config()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/seller")
def seller_required(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        rol = payload.get("rol")
        if rol != 2:
            raise CustomAppException(
                code_error=403, msg="No tienes permiso para acceder a esta ruta"
            )
        return payload
    except JWTError:
        raise CustomAppException(
            code_error=401, msg="Token inválido"
        )