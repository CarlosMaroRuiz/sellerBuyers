from sqlalchemy.orm import Session
from src.product.dao_product import ProductDAO
from src.shared.utils.custom_exeption import CustomAppException

def get_products_user(db: Session, user_id: int):
    try:
        productos = ProductDAO.get_products_by_user(db, user_id)
        return productos
    except CustomAppException as e:
        print(f"Error: {e.msg}")
