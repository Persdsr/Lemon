# Generated by Django 3.2.15 on 2022-10-01 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_alter_favoritepost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritepost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_favorite', to='food.post', verbose_name='Пост'),
            preserve_default=False,
        ),
    ]
