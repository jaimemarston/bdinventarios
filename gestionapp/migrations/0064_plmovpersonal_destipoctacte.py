# Generated by Django 2.0.8 on 2019-10-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0063_auto_20190930_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='plmovpersonal',
            name='destipoctacte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
