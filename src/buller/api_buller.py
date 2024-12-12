from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.buller.service_buller import handle_create_buyer
from src.db.session import get_db
from src.buller.schemas.buller_schema import Buyer
from src.buller.schemas.buyer_response import BuyerResponse

router_buyer = APIRouter(prefix="/api/users/buyer", tags=["Buyers"])

@router_buyer.post("/", response_model=BuyerResponse, status_code=201)
def create_buyer(buyer_data: Buyer, db: Session = Depends(get_db)):
    return handle_create_buyer(db, buyer_data)
