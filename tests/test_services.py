import pytest
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status

faker = Faker()

@pytest.fixture
def client_with_auth():
    client = APIClient()
    role_payload = {
        'name': 'ADMIN'
    }
    role = client.post('/api/roles/', role_payload, format='json')
    role_data = role.data
    assert role.status_code == status.HTTP_201_CREATED

    user_payload = {
        'username': faker.user_name(),
        'name': faker.name(),
        'email': faker.email(),
        'password': faker.password(),
        'role': role_data['id']
    }
    user = client.post('/api/users/', user_payload, format='json')
    assert user.status_code == status.HTTP_201_CREATED

    login_payload = {
        'username': user_payload['username'],
        'password': user_payload['password']
    }
    login = client.post('/api/auth/login/', login_payload, format='json')
    login_data = login.data
    assert login.status_code == status.HTTP_200_OK

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_data['access']}')
    return client

@pytest.mark.django_db
def test_create_service(client_with_auth):
    payload = {
        'name': 'Corte de cabello',
        'description': 'Corte de cabello de alta calidad',
        'price': 10.0,
        'duration': 1,
    }
    service = client_with_auth.post('/api/services/', payload, format='json')
    service_data = service.data
    assert service.status_code == status.HTTP_201_CREATED
    assert isinstance(service_data, dict)
    assert isinstance(service_data['id'], int)
    assert service_data['name'] == 'Corte de cabello'