# Generated by Django 3.2.5 on 2021-08-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=300, upload_to='img/'),
        ),
    ]
