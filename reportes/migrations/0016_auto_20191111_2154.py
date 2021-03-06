# Generated by Django 2.2.7 on 2019-11-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0015_pedido_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('ER', 'En repartición'), ('EN', 'Entregado'), ('CA', 'Cancelado')], default='EN', max_length=2),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
