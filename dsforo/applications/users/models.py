from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#managers
from .managers import UserManager


@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    email = models.EmailField('correo electronico', unique=True)
    first_name = models.CharField('nombres', max_length=50, blank=True)
    last_name = models.CharField('apellidos', max_length=50, blank=True)
    avatar = models.URLField(
        'foto',
        blank=True,
    )
    image = models.ImageField('Imagen de usuario', upload_to="users", blank=True, null=True)
    phone = models.CharField('telefono', max_length=50, blank=True, null=True)
    gender = models.CharField('sexo', max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField(blank=True, null=True)
    addresse = models.CharField('direccion',blank=True, max_length=100)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
