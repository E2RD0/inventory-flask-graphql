import graphene

class ProductType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Float()
    stock = graphene.Int()
    available = graphene.Boolean()
