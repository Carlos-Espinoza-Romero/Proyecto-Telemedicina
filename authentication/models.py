from django.db import models
from django.contrib.auth.models import User

class Roles(models.Model):
    ROLES = (
        ('ADMIN', 'ADMIN'),
        ('SELLER', 'SELLER'),
    )
    name = models.CharField(max_length=10, choices=ROLES)

class UserRoles(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='user_role'
    )
    role = models.OneToOneField(
        Roles,
        on_delete=models.CASCADE,
        db_column='role_id',
        related_name='user_role'
    )