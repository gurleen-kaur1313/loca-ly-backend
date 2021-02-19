import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import Jobs
from graphql import GraphQLError
from django.db.models import Q


class jobss(DjangoObjectType):
    class Meta:
        model = Jobs


class Query(graphene.ObjectType):
    alljobs = graphene.List(jobss)

    def resolve_alljobs(self, info):
        return Jobs.objects.all()

  




class AddJob(graphene.Mutation):
    newjob = graphene.Field(jobss)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        pay = graphene.Int()
        skillsrequired = graphene.String()
        mobile = graphene.String()
        location = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        jobadd=Jobs.objects.create(user=user)
        jobadd.title = kwargs.get("title")
        jobadd.description = kwargs.get("description")
        jobadd.pay = kwargs.get("pay")
        jobadd.skillsrequired = kwargs.get("skillsrequired")
        jobadd.mobile = kwargs.get("mobile")
        jobadd.location = kwargs.get("location")
        jobadd.save()
        return AddJob(newjob=jobadd)


class Mutation(graphene.ObjectType):
    add_job = AddJob.Field()