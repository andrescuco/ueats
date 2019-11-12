# Generated by Django 2.2.7 on 2019-11-12 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_auto_20191111_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='reportes.ProductoPedido'),
        ),
    ]