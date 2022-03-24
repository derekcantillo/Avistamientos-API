# Generated by Django 3.2.4 on 2022-03-24 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_clase_especie_familia_filo_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='especie',
            name='id_clase',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.clase'),
        ),
        migrations.AddField(
            model_name='especie',
            name='id_familia',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.familia'),
        ),
        migrations.AddField(
            model_name='especie',
            name='id_filo',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.filo'),
        ),
        migrations.AddField(
            model_name='especie',
            name='id_genero',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.genero'),
        ),
        migrations.AddField(
            model_name='especie',
            name='id_orden',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.orden'),
        ),
    ]
