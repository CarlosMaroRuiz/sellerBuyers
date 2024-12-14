from sqlalchemy.orm import Session
from src.product.dao_product import ProductDAO
from src.shared.utils.custom_exeption import CustomAppException

def buy_product_services(db: Session, product_id: str, quantity: int) -> dict:
    try:

        product = ProductDAO.get_product_by_name(db, product_id)
        result = ProductDAO.reduce_product_stock(db, product, quantity)

        return {
            "message": f"Compra realizada con éxito.",
            "product_status": result
        }
    except CustomAppException as e:
        raise e
    except Exception as e:
        raise CustomAppException(
            code_error=500,
            msg=f"Ocurrió un error al procesar la compra: {str(e)}"
        )