# Generated by Django 3.1.7 on 2021-03-26 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0014_auto_20210304_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='photo/'),
        ),
    ]
