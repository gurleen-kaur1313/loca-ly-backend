import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import Pgs
from graphql import GraphQLError
from django.db.models import Q
from location.models import Location


class pgss(DjangoObjectType):
    class Meta:
        model = Pgs


class Query(graphene.ObjectType):
    searchpgs = graphene.List(pgss, search=graphene.String())
    onepg = graphene.Field(pgss, pg_id=graphene.String())

    def resolve_searchpgs(self, info, search=None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        if search:
            filter = Q(rent__icontains=search) | Q(location__icontains=search) | Q(
                city__icontains=search) | Q(state__icontains=search)
            return Pgs.objects.filter(filter)
        return Exception("No PG")

    def resolve_by_id(root, info, pg_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Pgs.objects.get(id=pg_id)


class AddPG(graphene.Mutation):
    newpg = graphene.Field(pgss)

    class Arguments:
        usertype = graphene.String()
        roomtype = graphene.String()
        kitchen_available = graphene.String()
        washroom_attached = graphene.String()
        laundry_included = graphene.String()
        rent = graphene.Int()
        location = graphene.String()
        url = graphene.String()

    def mutate(self, info, location, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        pgadd = Pgs.objects.create(created_by=user)
        pgadd.usertype = kwargs.get("usertype")
        pgadd.roomtype = kwargs.get("roomtype")
        pgadd.kitchen_available = kwargs.get("kitchen_available")
        pgadd.washroom_attached = kwargs.get("washroom_attached")
        pgadd.laundry_included = kwargs.get("laundry_included")
        pgadd.rent = kwargs.get("rent")
        pgadd.url = kwargs.get("url")
        try:
            if location:
                filter = Q(city__icontains=location) | Q(
                    state__icontains=location)
            temp = Location.objects.filter(filter).first()
            # if temp:
            #     jobadd.rating=temp
            # else:
            #     temp2=Location.objects.create(city=location)
            #     jobadd.rating=temp2
        except:
            temp = Location.objects.create(city=location)
            temp.save()
        pgadd.location = temp
        pgadd.save()
        return AddPG(newpg=pgadd)


class Mutation(graphene.ObjectType):
    add_pg = AddPG.Field()
