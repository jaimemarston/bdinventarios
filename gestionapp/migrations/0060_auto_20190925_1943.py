# Generated by Django 2.0.8 on 2019-09-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0059_auto_20190925_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodetrecetas',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prodetrecetas',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='prodetrecetas',
            name='hrsfin',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='prodetrecetas',
            name='hrsini',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]