import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import Location
from graphql import GraphQLError
from django.db.models import Q


class locations(DjangoObjectType):
    class Meta:
        model = Location


class Query(graphene.ObjectType):
    alllocations = graphene.List(locations)
    onelocation = graphene.Field(locations, location_city=graphene.String())

    def resolve_alllocations(self, info):
        return Location.objects.all()

    def resolve_by_id(root, info, location_city):
        return Location.objects.get(city=location_city)


class IncrementLocation(graphene.Mutation):
    newlocation = graphene.Field(Location)

    class Arguments:
        city = graphene.String()
        rating = graphene.Int()

    def mutate(self, info, city, rating, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        try:
            if city:
                filter = Q(city__icontains=city)
            temp = Location.objects.filter(filter).first()
            temp.rating += rating
            temp.save()
        except:
            temp = Location.objects.create(city=city)
            temp.save()
        return temp


class DecrementLocation(graphene.Mutation):
    newlocation = graphene.Field(Location)

    class Arguments:
        city = graphene.String()
        rating = graphene.Int()

    def mutate(self, info, city, rating, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        try:
            if city:
                filter = Q(city__icontains=city)
            temp = Location.objects.filter(filter).first()
            temp.rating -= rating
            temp.save()
        except:
            temp = Location.objects.create(city=city)
            temp.save()
        return temp


class Mutation(graphene.ObjectType):
    # increment = IncrementLocation.Field()
    # deccrement = DecrementLocation.Field()
    pass