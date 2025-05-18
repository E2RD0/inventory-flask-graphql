import graphene
from api.queries import Query
from api.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
