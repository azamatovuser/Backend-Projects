# Generated by Django 4.1.6 on 2023-02-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
