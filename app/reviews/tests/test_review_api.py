"""
Test cases for Reviews APIs
"""
from django.test import Test
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import (
    Recipe,
    Review
)


def sample_user(email='test1@gmail.com', password='Welcome!1'):
    return get_user_model.objects.create_user(email=email, password=password)


def sample_recipe(user, **params):
    defaults = {
        'title': 'Sample recipe',
        'description': 'Sample description',
        'time_minutes': 10,
        'price': 5.00,
        'link': ''
    }
    defaults.update(params)
    
    return Recipe.objects.create(user=user, **defaults)

class PrivateReviewAPiTest():

    def setUp(self):
        self.user = sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)
    
    def test_create_review(self):
        recipe = sample_recipe()

        payload = {
            'recipe': recipe.id,
            'review': 'This is a test review'
        }
        res = self.client.post('review:user-reviews',payload)
        self.assertEqual(res.status_code, status.HTTP_200_CREATED)


