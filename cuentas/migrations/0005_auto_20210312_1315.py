# Generated by Django 3.1.1 on 2021-03-12 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_auto_20210312_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilino',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cuentas.departamento'),
        ),
    ]
