# Generated by Django 4.1.7 on 2023-02-28 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='parent_comment',
        ),
    ]
