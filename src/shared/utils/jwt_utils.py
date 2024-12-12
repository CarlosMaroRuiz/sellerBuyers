from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "infinite")

def create_access_token(data: dict):
    to_encode = data.copy()

    if ACCESS_TOKEN_EXPIRE_MINUTES.lower() != "infinite":
        try:
            expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
            to_encode.update({"exp": expire})
        except ValueError:
            raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES debe ser un número o 'infinite'.")


    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
