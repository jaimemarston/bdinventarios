# Generated by Django 2.0.8 on 2019-10-01 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0061_prorecetas_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodetproduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('codpro', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cc', models.CharField(blank=True, max_length=100, null=True)),
                ('descc', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('fechafin', models.DateField(blank=True, null=True)),
                ('turno', models.CharField(blank=True, max_length=15, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('importe', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('hrsini', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('hrsfin', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proproduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cc', models.CharField(blank=True, max_length=100, null=True)),
                ('descc', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('fechafin', models.DateField(blank=True, null=True)),
                ('turno', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='prodetproduccion',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movproduccion', to='gestionapp.Proproduccion'),
        ),
    ]
