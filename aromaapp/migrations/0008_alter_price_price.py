# Generated by Django 4.1.3 on 2022-12-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0007_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('9', '9')], max_length=10),
        ),
    ]
