from .models import User as UserModel
from django.test import TestCase
from graphene.test import Client
from server.schema import schema

class UserTypeTest(TestCase):
    def setUp(self):
        UserModel.objects.create_user(
            username='Bob',
            email='bob@bobtest.com',
            password='bobpassword',
            first_name='Bob'
        )
    
    def test_retrieve_user(self):
        client = Client(schema)
        result = client.execute('''
        {
            user(username: "Bob") {
                first_name
            }
        }
        ''')

        assert result['data']['user']['first_name'] == 'Bob'
