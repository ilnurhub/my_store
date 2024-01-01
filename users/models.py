from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    country = models.CharField(max_length=250, **NULLABLE, verbose_name='страна')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    secret_key = models.CharField(max_length=6, default=0, verbose_name='секретный ключ')
    is_active = models.BooleanField(default=False, verbose_name='статус')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
