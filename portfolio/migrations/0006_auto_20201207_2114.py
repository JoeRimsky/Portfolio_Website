# Generated by Django 3.1.2 on 2020-12-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20201207_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='Hello world!', max_length=50),
        ),
    ]
