import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    payload = {
        "username": "testuser",
        "password": "testpassword123",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
    }
    response = client.post('/api/auth/register/', payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['user']['username'] == 'testuser'

@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    User.objects.create_user(username='testuser', password='testpassword123')
    payload = {
        "username": "testuser",
        "password": "testpassword123"
    }
    response = client.post('/api/auth/login/', payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data
