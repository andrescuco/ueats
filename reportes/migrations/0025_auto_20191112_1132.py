# Generated by Django 2.2.7 on 2019-11-12 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0024_auto_20191112_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='pedido_asignado',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to='reportes.Pedido'),
        ),
    ]