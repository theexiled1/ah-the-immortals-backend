# Generated by Django 2.2 on 2019-05-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_notifications_subscription', models.BooleanField(default=True)),
                ('in_app_notifications_subscription', models.BooleanField(default=True)),
            ],
        ),
    ]
