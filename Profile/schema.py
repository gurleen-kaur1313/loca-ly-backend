from inspect import Arguments
from django.core.checks.messages import Info
import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import User, Profile
from graphql import GraphQLError
from django.db.models import Q


class Users(DjangoObjectType):
    class Meta:
        model = User


class MyProfile(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    allUsers = graphene.List(Users, id=graphene.String(required=True))
    me = graphene.Field(Users)
    myprofile = graphene.Field(MyProfile)

    def resolve_findUsers(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return User.objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return user

    def resolve_myprofile(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Profile.objects.get(user=active)


class CreateUser(graphene.Mutation):
    user = graphene.Field(Users)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, **kwargs):
        nuser = User(email=kwargs.get("email"))
        nuser.set_password(kwargs.get("password"))
        nuser.save()

        return CreateUser(user=nuser)


class CreateProfile(graphene.Mutation):
    profile = graphene.Field(MyProfile)

    class Arguments:
        name = graphene.String()
        mobile = graphene.String()
        location = graphene.String()
        age = graphene.Int()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        myProfile = Profile.objects.create(user=user)
        myProfile.name = kwargs.get("name")
        myProfile.mobile = kwargs.get("mobile")
        myProfile.location = kwargs.get("location")
        myProfile.Age = kwargs.get("age")
        myProfile.Gender = kwargs.get("gender")
        myProfile.save()

        return CreateProfile(profile=myProfile)


class UpdateProfile(graphene.Mutation):
    profile = graphene.Field(MyProfile)

    class Arguments:
        name = graphene.String()
        mobile = graphene.String()
        location = graphene.String()
        age = graphene.Int()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        myProfile = Profile.objects.get(user=user)
        myProfile.name = kwargs.get("name")
        myProfile.mobile = kwargs.get("mobile")
        myProfile.location = kwargs.get("location")
        myProfile.Age = kwargs.get("age")
        myProfile.Gender = kwargs.get("gender")
        myProfile.save()

        return UpdateProfile(profile=myProfile)





class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_profile = UpdateProfile.Field()
    create_profile = CreateProfile.Field()
