# Generated by Django 3.0 on 2019-12-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]