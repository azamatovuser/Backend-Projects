# Generated by Django 4.1.4 on 2022-12-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('image', models.ImageField(blank=True, help_text='2MB is limit', null=True, upload_to='articles')),
                ('content', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]