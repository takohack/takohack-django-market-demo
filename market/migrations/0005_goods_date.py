# Generated by Django 3.0 on 2019-12-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20191208_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
