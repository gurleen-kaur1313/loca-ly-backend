import graphene
import graphql_jwt
import job.schema
import Profile.schema
import security.schema
import pg.schema


class Query(job.schema.Query, Profile.schema.Query, security.schema.Query, pg.schema.Query, graphene.ObjectType):
    pass


class Mutation(job.schema.Mutation, Profile.schema.Mutation, security.schema.Mutation, pg.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
