# Generated by Django 3.0.7 on 2020-06-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200612_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
