# Generated by Django 4.1.7 on 2023-04-04 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0007_userprofileuploads_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='users_bookmarks',
            field=models.ManyToManyField(related_name='bookmarks', through='board.UserProfileUploads', to=settings.AUTH_USER_MODEL),
        ),
    ]
