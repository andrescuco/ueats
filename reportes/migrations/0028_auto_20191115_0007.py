# Generated by Django 2.2.7 on 2019-11-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0027_auto_20191114_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamo',
            name='resuelto',
        ),
        migrations.AddField(
            model_name='reclamo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='tipo',
            field=models.CharField(choices=[('I', 'Pedido incorrecto'), ('D', 'Pedido demorado'), ('N', 'Pedidio no llegó')], max_length=1),
        ),
    ]
