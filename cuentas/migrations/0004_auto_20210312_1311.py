# Generated by Django 3.1.1 on 2021-03-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_auto_20210312_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
