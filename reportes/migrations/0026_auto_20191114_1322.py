# Generated by Django 2.2.7 on 2019-11-14 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0025_auto_20191112_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='pedido_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reportes.Pedido'),
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('PI', 'Pedido incorrecto'), ('PD', 'Pedido demorado'), ('PN', 'Pedido no llegó')], max_length=1)),
                ('estado', models.BooleanField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Pedido')),
            ],
        ),
    ]