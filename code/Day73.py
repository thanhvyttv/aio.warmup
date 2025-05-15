from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Xin chào từ FastAPI!"}


@app.get("/add")
def add(a: int, b: int):
    return a + b


@app.get("/subtract")
def subtract(a: int, b: int):
    return a - b


@app.get("/multiply")
def multiply(a: int, b: int):
    return a * b


@app.get("/divide")
def divide(a: int, b: int):
    return a / b


user_db = [
    {"id": 1, "name": "John", "age": 13, "email": "join@test.com"},
    {"id": 2, "name": "Mark", "age": 20, "email": "markkk@test.com"},
    {"id": 3, "name": "Namtan", "age": 30, "email": "namtan@test.com"},
    {"id": 4, "name": "Film", "age": 25, "email": "film@test.com"},
]


class User(BaseModel):
    id: int | None = None
    name: str
    age: int
    email: str


@app.post("/user", response_model=bool)
def create_user(user: User):
    user.id = len(user_db)
    user_db.append(user)
    is_adult = False
    if user.age >= 18:
        is_adult = True
    return is_adult


products_db = [
    {"id": 1, "product_name": "Product A", "quantity": 10},
    {"id": 2, "product_name": "Product B", "quantity": 16},
]


class Product(BaseModel):
    id: int | None = None
    product_name: str
    quantity: int


@app.get("/products")
def get_product():
    return products_db


@app.post("/product", response_model=Product)
def create_product(product: Product):
    product.id = len(products_db)
    products_db.append(product)
    return product


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
