# Generated by Django 4.1.3 on 2022-12-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_bank_ıban'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesurname', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('debtType', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
