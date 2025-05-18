import graphene
from api.types import ProductType
from models.product_data import products

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):
        return products
