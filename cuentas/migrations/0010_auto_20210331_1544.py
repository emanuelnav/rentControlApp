# Generated by Django 3.1.1 on 2021-03-31 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0009_auto_20210331_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadocuenta',
            name='inquilino',
        ),
        migrations.AddField(
            model_name='inquilino',
            name='estadodecuenta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cuentas.estadocuenta'),
        ),
    ]
