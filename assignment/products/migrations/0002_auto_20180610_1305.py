# Generated by Django 2.0.6 on 2018-06-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='os_android',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='os_ios',
            field=models.BooleanField(default=False),
        ),
    ]