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

class PostView(models.Model):
    """Модель просмотров на постах"""
    post = models.ForeignKey('Post', verbose_name='Пост', on_delete=models.CASCADE, related_name='post_view')
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Tags(models.Model):
    """Теги постов"""
    name = models.CharField(verbose_name='Тег', max_length=20)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name

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
    slug = models.SlugField(verbose_name='URL')

    def get_absolute_url(self):
        return reverse('detail_food', kwargs={'food_slug': self.slug})

    def total_views(self):
        """Общее кол-во просмотров на посте"""
        return self.views.count()

    def __str__(self):
        return f'{self.title}'

class SeasonPost(Post):
    """Модель сезонных постов"""
    season_list = (
        ('Summer', 'Лето'),
        ('Winter', 'Зима'),
        ('Spring', 'Весна'),
        ('Autumn', 'Осень')
    )
    season = models.CharField(verbose_name='Сезон', choices=season_list, max_length=9)


class Comment(models.Model):
    """Комментарии к постам"""
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='post_comment')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='', max_length=155)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.author}'

    class Meta:
        ordering = ('-date',)

#class Ip(models.Model):
#    """Модель для сохранения IP пользователя"""
#    ip = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.ip