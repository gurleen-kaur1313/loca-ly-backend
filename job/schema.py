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
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Jobs.objects.all()



class AddJob(graphene.Mutation):
    newjob = graphene.Field(jobss)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        pay = graphene.Int()
        skillsrequired = graphene.String()
        minimumdesignation = graphene.String()
        mobile = graphene.String()
        location = graphene.String()
        jobtype = graphene.String()
        workfromhome = graphene.String()


    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        jobadd=Jobs.objects.create(user=user)
        jobadd.title = kwargs.get("title")
        jobadd.description = kwargs.get("description")
        jobadd.pay = kwargs.get("pay")
        jobadd.skillsrequired = kwargs.get("skillsrequired")
        jobadd.minimumdesignation = kwargs.get("minimumdesignation")
        jobadd.mobile = kwargs.get("mobile")
        jobadd.location = kwargs.get("location")
        jobadd.jobtype = kwargs.get("jobtype")
        jobadd.workfromhome = kwargs.get("workfromhome")
        jobadd.save()
        return AddJob(newjob=jobadd)


class Mutation(graphene.ObjectType):
    add_job = AddJob.Field()