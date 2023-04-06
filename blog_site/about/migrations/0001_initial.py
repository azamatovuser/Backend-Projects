# Generated by Django 4.1.3 on 2023-01-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=221)),
                ('position', models.CharField(max_length=221)),
                ('avatar', models.ImageField(upload_to='feedbacks/')),
                ('message', models.TextField()),
            ],
        ),
    ]
