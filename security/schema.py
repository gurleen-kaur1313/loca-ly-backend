import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import PoliceEmergency
from graphql import GraphQLError
from django.db.models import Q



class Police(DjangoObjectType):
    class Meta:
        model = PoliceEmergency


class Query(graphene.ObjectType):
    police = graphene.List(Police)
 
    def resolve_police(self,info):
        return PoliceEmergency.objects.all().order_by("-time")


class AddPoliceEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Police)

    class Arguments:
        location = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = PoliceEmergency.objects.create(user=user)
        test.location = kwargs.get("location")
        test.save()
        return AddPoliceEmergency(myEmergency=test)


class Mutation(graphene.ObjectType):
    add_police = AddPoliceEmergency.Field()