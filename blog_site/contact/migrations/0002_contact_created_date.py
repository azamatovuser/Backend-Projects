# Generated by Django 4.1.3 on 2023-01-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
