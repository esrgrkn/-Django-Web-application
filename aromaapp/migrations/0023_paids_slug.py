# Generated by Django 4.1.3 on 2022-12-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0022_remove_paids_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='paids',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
