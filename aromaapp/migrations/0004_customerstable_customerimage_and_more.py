# Generated by Django 4.1.3 on 2022-12-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aromaapp', '0003_alter_customerstable_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerstable',
            name='customerImage',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='customerstable',
            name='phoneNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customerstable',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
