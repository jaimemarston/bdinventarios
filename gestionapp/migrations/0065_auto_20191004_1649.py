# Generated by Django 2.0.8 on 2019-10-04 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0064_merge_20191004_1541'),
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
