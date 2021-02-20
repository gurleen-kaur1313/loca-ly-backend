import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import PoliceEmergency
from graphql import GraphQLError
from django.db.models import Q
from location.models import Location


class Police(DjangoObjectType):
    class Meta:
        model = PoliceEmergency


class Query(graphene.ObjectType):
    police = graphene.List(Police)

    def resolve_police(self, info):
        return PoliceEmergency.objects.all().order_by("-time")


class AddPoliceEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Police)

    class Arguments:
        location = graphene.String()

    def mutate(self, info, location, **kwargs):
        user = info.context.user
        test = PoliceEmergency.objects.create(user=user)
        try:
            if location:
                filter = Q(city__icontains=location) | Q(
                    state__icontains=location)
            temp = Location.objects.filter(filter).first()
            temp.rating += 2
            temp.save()
            # if temp:
            #     jobadd.rating=temp
            # else:
            #     temp2=Location.objects.create(city=location)
            #     jobadd.rating=temp2
        except:
            temp = Location.objects.create(city=location)
            temp.save()
        test.save()
        return AddPoliceEmergency(myEmergency=test)


class Mutation(graphene.ObjectType):
    add_police = AddPoliceEmergency.Field()
