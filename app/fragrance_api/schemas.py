from pydantic import BaseModel

class Success(BaseModel):
    message: str

class Error(BaseModel):
    message: str

class ProductSchemaOut(BaseModel):
    product_brand: str
    product_name: str
    product_price: float
    product_quantity: int
