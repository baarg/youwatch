# Generated by Django 3.1b1 on 2020-07-07 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_search_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='name',
            field=models.TextField(default='unNamed'),
        ),
    ]
