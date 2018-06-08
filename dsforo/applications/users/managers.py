from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def search_by_email(self,kword):
        return self.filter(
            is_active=True,
            email__startswith=kword,
        )[:20]


    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            raise ValueError("el email es obligatorio")

        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
