# Generated by Django 4.1.3 on 2022-12-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0019_alter_customerstable_phonenum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstable',
            name='phoneNum',
            field=models.IntegerField(),
        ),
    ]
