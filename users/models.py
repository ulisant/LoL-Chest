from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    """docstring for UserManager"""

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("The username is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    """docstring for User"""

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    summoner_name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    server = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    status = models.BooleanField(default=False)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username
