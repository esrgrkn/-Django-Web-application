# Generated by Django 4.1.3 on 2022-12-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0009_alter_producttable_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(),
        ),
    ]
