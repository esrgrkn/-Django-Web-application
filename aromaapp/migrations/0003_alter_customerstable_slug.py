# Generated by Django 4.1.3 on 2022-12-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0002_alter_producttable_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstable',
            name='slug',
            field=models.SlugField(),
        ),
    ]
