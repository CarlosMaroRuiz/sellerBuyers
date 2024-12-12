from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from src.config import Config
from src.shared.utils.custom_exeption import CustomAppException

config = Config()
oauth2_scheme_buyer = OAuth2PasswordBearer(tokenUrl="/api/auth/buyer")

def buyer_required(token: str = Depends(oauth2_scheme_buyer)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        rol = payload.get("rol")
        if rol != 1:
            raise CustomAppException(
                code_error=403, msg="No tienes permiso para acceder a esta ruta"
            )
        return payload
    except JWTError:
        raise CustomAppException(
            code_error=401, msg="Token inválido"
        )

