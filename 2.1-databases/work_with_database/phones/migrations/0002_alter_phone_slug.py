# Generated by Django 4.0.2 on 2022-02-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=models.CharField(max_length=60)),
        ),
    ]
