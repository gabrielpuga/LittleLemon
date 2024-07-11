from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token 

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser3', password='employee@123!')
        
        self.token = Token.objects.create(user=self.user)
        
        self.menu1 = Menu.objects.create(title="IceCream", price=1.00, inventory=100)
        self.menu3 = Menu.objects.create(title="Tamal", price=2.75, inventory=75)

    def test_getall(self):
        
        client = APIClient()
        
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        response = client.get(reverse('menu-list'))  # 'menu-list' is the URL name for MenuItemsView
        #print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = MenuSerializer([self.menu1, self.menu2, self.menu3], many=True).data

        self.assertEqual(response.data, expected_data)
        