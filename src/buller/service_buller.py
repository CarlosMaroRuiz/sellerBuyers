from sqlalchemy.orm import Session
from src.db.models.user_model import User
from src.buller.schemas.buyer_response import BuyerResponse
from src.buller.schemas.buller_schema import Buyer
from src.shared.schemas.error_schema import ErrorResponse
from src.shared.utils.custom_exeption import CustomAppException
from src.shared.utils.hash import hash_password
import logging

logger = logging.getLogger(__name__)

def handle_create_buyer(db: Session, buyer_data: Buyer) -> BuyerResponse | ErrorResponse:
    existing_user = db.query(User).filter(User.email == buyer_data.email).first()
    if existing_user:
        if existing_user:
            logger.info(f"Usuario existente encontrado: {existing_user.email}")
            raise CustomAppException(
                code_error=1001,
                msg=f"El usuario con el correo '{buyer_data.email}' ya está registrado."
            )

    hashed_password = hash_password(buyer_data.password)

    new_buyer = User(
        username=buyer_data.username,
        email=buyer_data.email,
        password=hashed_password,
        idRol=buyer_data.idRol
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return BuyerResponse(
        username=new_buyer.username,
        message="Buyer creado exitosamente"
    )
