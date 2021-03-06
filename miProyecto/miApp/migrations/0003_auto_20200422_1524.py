# Generated by Django 3.0.5 on 2020-04-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='codigo',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='componente',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]
