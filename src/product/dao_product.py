from sqlalchemy.orm import Session
from src.db.models.product_model import Product
from src.shared.utils.custom_exeption import CustomAppException

class ProductDAO:
    @staticmethod
    def create_product(db: Session, product_data: dict) -> Product:
        try:
            new_product = Product(**product_data)
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return new_product
        except Exception as e:
            db.rollback()
            raise CustomAppException(
                code_error=500,
                msg=f"Ocurrió un error al crear el producto: {str(e)}"
            )

    @staticmethod
    def get_products_by_user(db: Session, user_id: int) -> list[Product]:
        try:
            products = db.query(Product).filter(Product.idUser == user_id).all()
            if not products:
                raise CustomAppException(
                    code_error=404,
                    msg=f"No se encontraron productos para el usuario con ID {user_id}."
                )
            return products
        except Exception as e:
            raise CustomAppException(
                code_error=500,
                msg=f"Ocurrió un error al obtener los productos: {str(e)}"
            )

    @staticmethod
    def get_product_by_name(db: Session, product_name: str) -> Product:
        try:
            product = db.query(Product).filter(Product.name == product_name).first()
            if not product:
                raise CustomAppException(
                    code_error=404,
                    msg=f"Producto con nombre '{product_name}' no encontrado."
                )
            return product
        except Exception as e:
            raise CustomAppException(
                code_error=500,
                msg=f"Ocurrió un error al buscar el producto: {str(e)}"
            )

    @staticmethod
    def reduce_product_stock(db: Session, product: Product, quantity: int) -> dict:
        try:
            if product.stoke < quantity:
                raise CustomAppException(
                    code_error=400,
                    msg=f"Cantidad no disponible. Stock actual: {product.stoke}"
                )

            product.stoke -= quantity
            total = quantity * product.price
            if product.stoke <= 0:
                db.delete(product)
                db.commit()
                return {"name": product.name, "status": "Producto agotado y eliminado","total":total}

            db.commit()
            db.refresh(product)
            return {"name": product.name, "total":total}
        except CustomAppException as e:
            raise e
        except Exception as e:
            db.rollback()
            raise CustomAppException(
                code_error=500,
                msg=f"Ocurrió un error al reducir el stock del producto: {str(e)}"
            )
