# Generated by Django 3.2.9 on 2021-12-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(upload_to='media/con/'),
        ),
    ]
