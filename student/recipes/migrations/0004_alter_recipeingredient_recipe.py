# Generated by Django 4.1.4 on 2023-01-05 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_tag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe'),
        ),
    ]
