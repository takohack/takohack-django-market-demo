# Generated by Django 3.0 on 2019-12-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_goods_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]