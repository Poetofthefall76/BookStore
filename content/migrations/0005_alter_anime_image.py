# Generated by Django 3.2.9 on 2021-12-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_anime_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
