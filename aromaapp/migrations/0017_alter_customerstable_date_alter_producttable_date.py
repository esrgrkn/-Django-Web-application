# Generated by Django 4.1.3 on 2022-12-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0016_alter_customerstable_date_alter_producttable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstable',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]