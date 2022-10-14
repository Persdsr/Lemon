from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель юзера"""
    first_name = models.CharField(verbose_name='Имя', max_length=33, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=33, null=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', null=True, blank=True, upload_to='avatar_images/')
    about_me = models.TextField(verbose_name='Обо мне', max_length=200, blank=True, default='')
    profile_image = models.ImageField(verbose_name='Изображение в профиле', upload_to='profile_images/', blank=True)

    @property
    def get_image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '../../media/avatar_images/default_avatar.jpg'


class Contact(models.Model):
    """Модель подписки на email"""
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name