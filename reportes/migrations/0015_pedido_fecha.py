# Generated by Django 2.2.7 on 2019-11-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0014_repartidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]