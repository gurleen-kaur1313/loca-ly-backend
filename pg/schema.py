import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import Pgs
from graphql import GraphQLError
from django.db.models import Q


class pgss(DjangoObjectType):
    class Meta:
        model = Pgs


class Query(graphene.ObjectType):
    searchpgs = graphene.List(pgss,search=graphene.String())
    onepg = graphene.Field(pgss, pg_id=graphene.String())

    def resolve_searchpgs(self, info, search=None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        if search:
            filter = Q(rent__icontains=search) | Q(locality__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search)
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
        description = graphene.String()
        rent = graphene.Int()
        locality = graphene.String()
        city = graphene.String()
        state = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        pgadd = Jobs.objects.create(user=user)
        pgadd.usertype = kwargs.get("usertype")
        pgadd.roomtype = kwargs.get("roomtype")
        pgadd.kitchen_available = kwargs.get("kitchen_available")
        pgadd.washroom_attached = kwargs.get("washroom_attached")
        pgadd.laundry_included = kwargs.get("laundry_included")
        pgadd.description = kwargs.get("description")
        pgadd.rent = kwargs.get("rent")
        pgadd.locality = kwargs.get("locality")
        pgadd.city = kwargs.get("city")
        pgadd.state = kwargs.get("state")
        pgadd.save()
        return AddPG(newpg=pgadd)


class Mutation(graphene.ObjectType):
    add_pg = AddPG.Field()