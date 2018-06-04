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
        query {
            user(username: "Bob") {
                username
            }
        }
        ''')

        print(result['errors'])

        assert result['data']['user']['username'] == 'Bob'

    def test_retrieve_all_users(self):
        client = Client(schema)
        result = client.execute('''
        query {
            allUsers(username: "Bob") {
                username
            }
        }
        ''')
        
        assert result['data'] is not None