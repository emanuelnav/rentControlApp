# Generated by Django 3.1.1 on 2021-03-16 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0005_auto_20210312_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilino',
            name='celular',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
    ]
