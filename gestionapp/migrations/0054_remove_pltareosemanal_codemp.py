# Generated by Django 2.0.8 on 2019-08-23 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0053_auto_20190823_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pltareosemanal',
            name='codemp',
        ),
    ]
