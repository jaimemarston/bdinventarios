# Generated by Django 2.0.8 on 2019-09-10 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0057_auto_20190910_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plmovpersonal',
            name='destipoctacte',
        ),
        migrations.RemoveField(
            model_name='plmovpersonal',
            name='tipoctacte',
        ),
    ]
