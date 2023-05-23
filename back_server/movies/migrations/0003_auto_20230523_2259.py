# Generated by Django 3.2 on 2023-05-23 13:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='users',
            field=models.ManyToManyField(related_name='liked_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
