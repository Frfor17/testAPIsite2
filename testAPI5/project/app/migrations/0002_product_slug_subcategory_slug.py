# Generated by Django 5.1.4 on 2025-01-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='a', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='a', max_length=255),
        ),
    ]