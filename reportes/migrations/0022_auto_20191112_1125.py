# Generated by Django 2.2.7 on 2019-11-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0021_auto_20191112_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='pedido_asignado',
            field=models.OneToOneField(default='-1', on_delete=django.db.models.deletion.CASCADE, to='reportes.Pedido'),
        ),
    ]
