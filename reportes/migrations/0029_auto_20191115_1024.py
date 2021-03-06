# Generated by Django 2.2.7 on 2019-11-15 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0028_auto_20191115_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='tipo',
            field=models.CharField(choices=[('I', 'Pedido incorrecto'), ('D', 'Pedido demorado'), ('N', 'Pedido no llegó')], max_length=1),
        ),
    ]
