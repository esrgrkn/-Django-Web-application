# Generated by Django 4.1.3 on 2022-12-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0008_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
