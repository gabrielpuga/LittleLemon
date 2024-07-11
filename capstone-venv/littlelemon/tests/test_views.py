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
        # Create a test user
        self.user = User.objects.create_user(username='testuser3', password='employee@123!')
         # Generate a new token
        self.token = Token.objects.create(user=self.user)
        # Create test instances of Menu model
        self.menu1 = Menu.objects.create(title="IceCream", price=1.00, inventory=100)
        self.menu2 = Menu.objects.create(title="Pizza", price=10.50, inventory=50)
        self.menu3 = Menu.objects.create(title="Burger", price=5.75, inventory=75)

    def test_getall(self):
        # Initialize Django Rest Framework APIClient
        client = APIClient()

        # Set Authorization header with the token
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Make GET request to retrieve all Menu objects
        response = client.get(reverse('menu-list'))  # Assuming 'menuitems-list' is the URL name for MenuItemsView
        # Print response content for debugging
        print(response.content)

        # Assert that response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize data
        expected_data = MenuSerializer([self.menu1, self.menu2, self.menu3], many=True).data

        # Assert that serialized data equals response data
        self.assertEqual(response.data, expected_data)
        