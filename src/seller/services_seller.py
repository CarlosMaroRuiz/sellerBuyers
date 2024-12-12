from sqlalchemy.orm import Session
from src.db.models.user_model import User
from src.seller.schemas.seller_model import Seller
from src.seller.schemas.seller_reponse import Seller_response
from src.shared.schemas.error_schema import ErrorResponse
from src.shared.utils.custom_exeption import CustomAppException
from src.shared.utils.hash import hash_password
import logging

logger = logging.getLogger(__name__)

def handle_create_seller(db: Session, seller_data: Seller) -> Seller_response | ErrorResponse:

    existing_user = db.query(User).filter(User.email == seller_data.email).first()
    print("entrooooo")
    if existing_user:
        if existing_user:
            logger.info(f"Usuario existente encontrado: {existing_user.email}")
            raise CustomAppException(
                code_error=1001,
                msg=f"El usuario con el correo '{seller_data.email}' ya está registrado."
            )

    hashed_password = hash_password(seller_data.password)

    new_buyer = User(
        username=seller_data.username,
        email=seller_data.email,
        password=hashed_password,
        idRol=seller_data.idRol
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return Seller_response(
        username=new_buyer.username,
        message="Buyer creado exitosamente"
    )
