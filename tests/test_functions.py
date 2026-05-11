import pytest
from faker import Faker

faker = Faker()

def division(a, b):
    return a / b

# Pruebas negativas
def test_division_error():
    # Verificar que al dividir por cero, Python lance un error correctamente
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

# Pruebas parametrizadas
@pytest.mark.parametrize("email, expected" , [
    ("test@gmail.com", True),
    ("user.name@example.com", True),
    ("invalid-email", False),
    ("@gmail.com", False),
])
def test_validate_email(email, expected):
    result = "@" in email and "." in email.split("@")[-1]
    assert result == expected


# Fixtures
@pytest.fixture
def base_user():
    return {
        'id': faker.random_int(),
        'username': faker.user_name(),
        'role': faker.random_element(['ADMIN', 'SELLER']),
        'is_active': faker.boolean()
    }

def test_active_user(base_user):
    assert base_user['is_active'] is True

def test_change_username(base_user):
    base_user['username'] = 'new_username'
    assert base_user['username'] == 'new_username'

def test_products_lists():
    products = ["zapatillas", "pantalones", "gorras"]

    assert "zapatillas" in products
    assert len(products) == 3
    assert "calzetines" not in products