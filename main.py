from fastapi import FastAPI
from src.buller.api_buller import router_buyer
from src.buller_auth.api_buller_auth import router_auth_buyer
from src.seller.api_seller import router_seller
from src.seller_auth.api_seller_auth import router_auth_seller
from src.product.api_product import router_product
from src.db.config import engine
from src.db.models.base import  Base
from src.shared.middlewares.exeption_middleware import exception_middleware

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)

app.middleware("http")(exception_middleware)

app.include_router(router_buyer)
app.include_router(router_seller)
app.include_router(router_auth_buyer)
app.include_router(router_auth_seller)
app.include_router(router_product)
#gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:5000 --daemon
