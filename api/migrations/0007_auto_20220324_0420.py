# Generated by Django 3.2.4 on 2022-03-24 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220324_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['name'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['name'], 'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
    ]
