# Generated by Django 4.0.4 on 2022-06-28 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discente', '0002_discente_email_discente_senha_discente_serie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discente',
            name='senha',
        ),
    ]
