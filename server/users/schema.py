from .models import User as UserModel
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

class UserType(DjangoObjectType):

    class Meta:
        model = UserModel
        interfaces = (graphene.Node, )
        only_fields = ('username', 'first_name')
        filter_fields = ['username', ]

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = UserModel(username)
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, username=graphene.String())
    all_users = DjangoFilterConnectionField(UserType)

    def resolve_user(self, args, ctx, info):
        username = args.get('username')

        if username is not None:
            return UserModel.objects.get(username=username)
        
        return None