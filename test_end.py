import requests

# Base URL de la API
BASE_URL = "http://127.0.0.1:8000/api"

#
seller_data = {
    "username": "seller2",
    "email": "seller2@example.com",
    "password": "password123",
    "idRol": 2
}

buyer_data = {
    "username": "buyer2",
    "email": "buyer2@example.com",
    "password": "password123",
    "idRol": 1
}

product_data = {
    "name": "Product1",
    "price": 100.50,
    "stoke": 50
}

# Crear vendedor
def create_seller():
    response = requests.post(f"{BASE_URL}/users/seller/", json=seller_data)
    if response.status_code == 201:
        print("Vendedor creado exitosamente.")
    else:
        print("Error al crear el vendedor:", response.json())

# Crear cliente
def create_buyer():
    response = requests.post(f"{BASE_URL}/users/buyer/", json=buyer_data)
    if response.status_code == 201:
        print("Cliente creado exitosamente.")
    else:
        print("Error al crear el cliente:", response.json())

# Autenticar vendedor
def authenticate_seller():
    auth_data = {
        "email": seller_data["email"],
        "password": seller_data["password"]
    }
    response = requests.post(f"{BASE_URL}/auth/seller", json=auth_data)
    if response.status_code == 200:
        token = response.json()["access_token"]
        print("Vendedor autenticado exitosamente.")
        return token
    else:
        print("Error al autenticar al vendedor:", response.json())
        return None

# Crear producto
def create_product(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{BASE_URL}/products/", json=product_data, headers=headers)
    if response.status_code == 201:
        print("Producto creado exitosamente:", response.json())
    else:
        print("Error al crear el producto:", response.json())

if __name__ == "__main__":
    # Paso 1: Crear vendedor
    create_seller()

    # Paso 2: Crear cliente
    create_buyer()

    # Paso 3: Autenticar vendedor
    token = authenticate_seller()

    if token:
        # Paso 4: Crear producto
        create_product(token)
