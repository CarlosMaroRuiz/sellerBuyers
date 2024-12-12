from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.product.dao_product import ProductDAO
from src.product.schemas.product_reponse import ProductResponse
from src.product.schemas.product_schema import ProductCreate
from src.db.session import get_db
from src.auth.verify_seller import seller_required
from src.product.services import listar_productos_de_usuario
from src.shared.utils.custom_exeption import CustomAppException

router_product = APIRouter(prefix="/api/products", tags=["products"])

@router_product.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    data_product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(seller_required)
):
    print(current_user.get("id_user"))
    try:
        if current_user.get("rol") != 2:
            raise CustomAppException(
                code_error=403,
                msg="No tienes permisos para realizar esta acción"
            )


        product_data = data_product.dict()
        product_data["idUser"] = current_user.get("id_user")

        new_product = ProductDAO.create_product(db, product_data)
        return new_product
    except CustomAppException as e:
        raise e
    except Exception as e:

        raise CustomAppException(
            code_error=500,
            msg=f"Ocurrió un error al crear el producto: {str(e)}"
        )

@router_product.get("/", response_model=list[ProductResponse], status_code=200)
def get_user_products(
    db: Session = Depends(get_db),
    current_user: dict = Depends(seller_required)
):
    try:
        if current_user.get("rol") != 2:
            raise CustomAppException(
                code_error=403,
                msg="No tienes permisos para realizar esta acción"
            )
        user_id = current_user.get("id_user")
        products = listar_productos_de_usuario(db,user_id)
        return products
    except CustomAppException as e:
        raise e
