# Generated by Django 4.2.4 on 2023-08-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_body_article_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
