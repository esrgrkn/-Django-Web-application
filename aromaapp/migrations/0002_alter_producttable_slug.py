# Generated by Django 4.1.3 on 2022-12-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='slug',
            field=models.SlugField(),
        ),
    ]
