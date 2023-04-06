# Generated by Django 4.1.6 on 2023-02-07 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('podcast', '0002_remove_podcast_comments_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcast.podcast')),
            ],
        ),
        migrations.AddField(
            model_name='podcast',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='podcast.comment'),
            preserve_default=False,
        ),
    ]
