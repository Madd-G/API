# Generated by Django 3.1.7 on 2021-03-02 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='goods_picture',
        ),
    ]
