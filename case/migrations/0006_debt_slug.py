# Generated by Django 4.1.3 on 2022-12-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_debt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
