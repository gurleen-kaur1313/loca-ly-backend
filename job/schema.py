import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import Jobs
from graphql import GraphQLError
from django.db.models import Q
from location.models import Location

class jobss(DjangoObjectType):
    class Meta:
        model = Jobs

class locations(DjangoObjectType):
    class Meta:
        model = Location

class Query(graphene.ObjectType):
    alljobs = graphene.List(jobss)
    searchjobs = graphene.List(jobss,search=graphene.String())
    onejob = graphene.Field(jobss, job_id=graphene.String())

    def resolve_alljobs(self,info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Jobs.objects.all()


    def resolve_searchjobs(self, info, search=None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        if search:
            filter = Q(title__icontains=search) | Q(description__icontains=search) | Q(skillsrequired__icontains=search) | Q(pay__icontains=search) | Q(minimumdesignation__icontains=search) | Q(location__icontains=search)
            return Jobs.objects.filter(filter)
        return Exception("No Job")


    def resolve_by_id(root, info, job_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Jobs.objects.get(id=job_id)
        



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

    def mutate(self, info, location,**kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        jobadd = Jobs.objects.create(user=user)
        jobadd.title = kwargs.get("title")
        jobadd.description = kwargs.get("description")
        jobadd.pay = kwargs.get("pay")
        jobadd.skillsrequired = kwargs.get("skillsrequired")
        jobadd.minimumdesignation = kwargs.get("minimumdesignation")
        jobadd.mobile = kwargs.get("mobile")
        jobadd.location = kwargs.get("location")
        jobadd.jobtype = kwargs.get("jobtype")
        jobadd.workfromhome = kwargs.get("workfromhome")
        try:
            if location:
                filter = Q(city__icontains=location) | Q(state__icontains=location) 
            temp = Location.objects.filter(filter).first()
            temp.rating-=1
            temp.save()
            # if temp:
            #     jobadd.rating=temp
            # else:
            #     temp2=Location.objects.create(city=location)
            #     jobadd.rating=temp2
        except:
            temp=Location.objects.create(city=location)
        jobadd.rating=temp
        jobadd.save()
        return AddJob(newjob=jobadd)


class Mutation(graphene.ObjectType):
    add_job = AddJob.Field()
