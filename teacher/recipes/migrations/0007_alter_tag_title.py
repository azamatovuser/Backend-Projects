# Generated by Django 4.1.4 on 2023-01-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipeingredient_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=221, unique=True),
        ),
    ]
