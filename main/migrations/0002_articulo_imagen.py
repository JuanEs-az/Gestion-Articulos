# Generated by Django 3.0.9 on 2020-08-29 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
