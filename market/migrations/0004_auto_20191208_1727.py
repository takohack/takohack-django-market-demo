# Generated by Django 3.0 on 2019-12-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20191208_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='goods',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
