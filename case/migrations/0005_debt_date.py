# Generated by Django 4.1.3 on 2022-12-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
