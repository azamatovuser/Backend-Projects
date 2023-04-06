# Generated by Django 4.1.6 on 2023-02-09 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_remove_podcast_comments_remove_podcast_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='podcast.podcast'),
        ),
    ]
