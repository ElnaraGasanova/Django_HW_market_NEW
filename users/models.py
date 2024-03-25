from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='users/avatar', verbose_name="Аватар", help_text="Загрузите фото",
                               **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', help_text='Укажите номер телефона',
                             **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', help_text='Укажите страну',
                               **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email', help_text="Укажите почту")
    token = models.CharField(max_length=50, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
