# Generated by Django 3.2 on 2021-07-17 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20210716_2106'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auth_user',
        ),
    ]