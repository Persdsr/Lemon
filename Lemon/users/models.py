from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Создание собственной модели юзера"""
    first_name = models.CharField(verbose_name='Имя', max_length=33, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=33, null=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', null=True, blank=True)
    about_me = models.TextField(verbose_name='Обо мне', max_length=200, blank=True, default='')

    @property
    def get_image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            pass
