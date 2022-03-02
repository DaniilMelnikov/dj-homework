# Generated by Django 4.0.2 on 2022-03-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='scopes',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.Article'),
        ),
    ]
