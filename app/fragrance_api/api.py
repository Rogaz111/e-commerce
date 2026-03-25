from ninja.security import HttpBearer
from ninja_extra import NinjaExtraAPI, api_controller, route

from app.fragrance_api.schemas import ProductSchemaOut, Error

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "5e681bb9-a52a-4ded-a942-6e51418971d2":
            return token

auth = GlobalAuth()
api = NinjaExtraAPI(auth=auth)

@api_controller(
    "products",
    tags=["Products"],
    permissions=[]
)

class ProductsController:
    @route.get("/all-products/", response={200: ProductSchemaOut, 400: Error, 404: Error})
    def get_products(self):
        return 200, ProductSchemaOut(
            product_brand="Bella",
            product_name="Bella",
            product_price=1000,
            product_quantity=10
        )


api.register_controllers(ProductsController)