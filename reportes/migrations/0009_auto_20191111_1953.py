# Generated by Django 2.2.7 on 2019-11-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0008_auto_20191111_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='reportes.ProductoPedido'),
        ),
    ]
