# Generated by Django 3.2.18 on 2023-05-24 01:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_otts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Otts',
            new_name='Ott',
        ),
    ]
