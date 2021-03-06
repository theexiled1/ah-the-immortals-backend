# Generated by Django 2.2 on 2019-05-16 06:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
        ('highlights', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='highlight',
            unique_together={('user', 'article', 'field', 'start_index', 'end_index')},
        ),
    ]
