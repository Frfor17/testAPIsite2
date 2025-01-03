from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Cart, CartItem
from rest_framework_simplejwt.tokens import RefreshToken


class CartViewSetTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='password123')


        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_post_cart(self):

        url = '/cart/'


        data = {
            'items': [
                {
                    'product': 1,
                    'quantity': 2
                },
                {
                    'product': 2,
                    'quantity': 3
                }
            ]
        }


        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        self.assertEqual(Cart.objects.count(), 1)


        cart = Cart.objects.first()
        self.assertEqual(cart.user.username, 'testuser')
        self.assertEqual(len(cart.items.all()), 2)

    def test_post_cart_unauthenticated(self):

        url = '/cart/'


        data = {
            'items': [
                {
                    'product': 1,
                    'quantity': 2
                }
            ]
        }


        response = self.client.post(url, data)


        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

