# Generated by Django 3.0.4 on 2020-04-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0003_auto_20200422_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='codigo',
            field=models.CharField(default='', max_length=20),
        ),
    ]
