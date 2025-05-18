import graphene
from api.types import ProductType
from models.product_data import products, update_product_stock


class UpdateStock(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int(required=True)
        quantity = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, product_id: int, quantity: int):
        if quantity == 0:
            raise Exception("Quantity must be non-zero.")

        for product in products:
            if product['id'] == product_id:
                updated = update_product_stock(product, quantity)
                return UpdateStock(product=updated)

        raise Exception(f"Product with ID {product_id} not found.")


class AddProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        stock = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name, price, stock):
        for prod in products:
            if prod['id'] == id:
                raise Exception(f"Product with ID {id} already exists.")

        new_product = {
            "id": id,
            "name": name,
            "price": price,
            "stock": stock,
            "available": stock > 0
        }

        products.append(new_product)
        return AddProduct(product=new_product)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, product_id: int):
        global products
        for product in products:
            if product['id'] == product_id:
                products.remove(product)
                return DeleteProduct(ok=True)

        raise Exception(f"Product with ID {product_id} not found.")


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        price = graphene.Float()

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name=None, price=None):
        for product in products:
            if product['id'] == id:
                if name is not None:
                    product['name'] = name
                if price is not None:
                    product['price'] = price
                return UpdateProduct(product=product)

        raise Exception(f"Product with ID {id} not found.")


class Mutation(graphene.ObjectType):
    updateStock = UpdateStock.Field()
    addProduct = AddProduct.Field()
    deleteProduct = DeleteProduct.Field()
    updateProduct = UpdateProduct.Field()
