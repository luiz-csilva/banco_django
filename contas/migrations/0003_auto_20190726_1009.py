# Generated by Django 2.2.3 on 2019-07-26 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_auto_20190726_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='data_de_criacao',
        ),
    ]
