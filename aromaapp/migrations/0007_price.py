# Generated by Django 4.1.3 on 2022-12-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0006_alter_customerstable_customerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('9', '9')])),
            ],
        ),
    ]
