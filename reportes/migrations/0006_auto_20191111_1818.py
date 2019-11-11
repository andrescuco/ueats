# Generated by Django 2.2.7 on 2019-11-11 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0005_producto_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Restaurante'),
        ),
    ]
