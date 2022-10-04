from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

from users.models import User


class PostStep(models.Model):
    """Модель шагов для постов"""
    post = models.ForeignKey('Post', verbose_name='Пост', on_delete=models.SET_NULL, null=True, related_name='post_step')
    title = models.CharField(verbose_name='Название шага', max_length=50)
    text = models.TextField(verbose_name='Текс')
    image = models.ImageField(verbose_name='Изображение', upload_to='post_step/', blank=True, null=True)

    def __str__(self):
        return f'{self.post} - {self.title}'

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'

class Tags(models.Model):
    """Теги постов"""
    name = models.CharField(verbose_name='Тег', max_length=20)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    """Модель постов"""
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(verbose_name='Название', max_length=155)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='post/')
    ingredients = RichTextField()
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_preparing = models.CharField(verbose_name='Время приготовления', max_length=10)
    tags = models.ManyToManyField(Tags, related_name='post_tags', blank=True)
    views = models.ManyToManyField(User, verbose_name='post_views', blank=True, related_name='post_views')
    favorite = models.ManyToManyField(User, verbose_name='Добавившие в избранное', blank=True, related_name='favorite_posts')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='post_category', on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL')

    def get_absolute_url(self):
        return reverse('detail_food', kwargs={'food_slug': self.slug})

    def total_views(self):
        """Общее кол-во просмотров на посте"""
        return self.views.count()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class SeasonPost(Post):
    """Модель сезонных постов"""
    season_list = (
        ('Summer', 'Лето'),
        ('Winter', 'Зима'),
        ('Spring', 'Весна'),
        ('Autumn', 'Осень')
    )
    season = models.CharField(verbose_name='Сезон', choices=season_list, max_length=9)

    class Meta:
        verbose_name = 'Сезонный пост'
        verbose_name_plural = 'Сезонные посты'

class Comment(models.Model):
    """Комментарии к постам"""
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='post_comment')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='', max_length=155)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
        ordering = ('-date',)

#class Ip(models.Model):
#    """Модель для сохранения IP пользователя"""
#    ip = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.ip