from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.seller_auth.schemas.Seller_login import Seller_Login
from src.shared.utils.custom_exeption import CustomAppException
from src.shared.utils.hash import verify_password
from src.db.models.user_model import User
from src.shared.utils.jwt_utils import create_access_token

router_auth_seller = APIRouter(prefix="/api/auth/seller", tags=["Auth seller"])

@router_auth_seller.post("/")
def login_seller(login_data: Seller_Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user:
        raise CustomAppException(code_error=400, msg="Credenciales inválidas")

    if not verify_password(login_data.password, user.password):
        raise CustomAppException(code_error=400, msg="Credenciales inválidas")

    if user.idRol != 2:
        raise CustomAppException(code_error=400, msg="Acceso denegado para este rol")

    access_token = create_access_token(data={"rol": user.idRol, "id_user": user.id})
    return {"access_token": access_token}
