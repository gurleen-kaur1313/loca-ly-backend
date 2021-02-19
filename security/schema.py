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
        locality = graphene.String()
        city = graphene.String()
        state = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = PoliceEmergency.objects.create(user=user)
        test.locality = kwargs.get("locality")
        test.city = kwargs.get("city")
        test.state = kwargs.get("state")
        test.save()
        return AddPoliceEmergency(myEmergency=test)


class Mutation(graphene.ObjectType):
    add_police = AddPoliceEmergency.Field()