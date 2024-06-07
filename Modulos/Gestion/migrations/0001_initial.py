# Generated by Django 5.0.6 on 2024-06-07 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('IdAdministrador', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=35)),
                ('Apellido', models.CharField(max_length=35)),
                ('Correo', models.EmailField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Bodegas',
            fields=[
                ('IdBodega', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=35)),
                ('Ubicacion', models.CharField(max_length=35)),
                ('Contacto', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('IdCliente', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=50)),
                ('Celular', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('IdProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=35)),
                ('Ciudad', models.CharField(max_length=35)),
                ('Celular', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('IdCompra', models.AutoField(primary_key=True, serialize=False)),
                ('FechaCompra', models.DateField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Proveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('IdVenta', models.AutoField(primary_key=True, serialize=False)),
                ('FechaPedido', models.DateField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('IdPagos', models.AutoField(primary_key=True, serialize=False)),
                ('MetodoPago', models.CharField(max_length=35)),
                ('FechaPago', models.DateField()),
                ('Venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Vinos',
            fields=[
                ('IdVino', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=35)),
                ('Año', models.CharField(max_length=35)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Stock', models.IntegerField()),
                ('Bodegas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.bodegas')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('IdDetalleVenta', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('PrecioUnitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.venta')),
                ('Vinos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.vinos')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('IdDetalleCompra', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('PrecioCompra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.compra')),
                ('Vinos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.vinos')),
            ],
        ),
    ]
