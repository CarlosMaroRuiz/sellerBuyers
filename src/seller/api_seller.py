from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.seller.schemas.seller_model import Seller
from src.seller.schemas.seller_reponse import Seller_response
from src.seller.services_seller import handle_create_seller

router_seller = APIRouter(prefix="/api/users/seller", tags=["Sellers"])

@router_seller.post("/", response_model=Seller_response, status_code=201)
def create_seller(seller_data: Seller, db: Session = Depends(get_db)):

    return handle_create_seller(db, seller_data)
