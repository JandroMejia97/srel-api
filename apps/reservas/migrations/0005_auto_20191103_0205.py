# Generated by Django 2.2.6 on 2019-11-03 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_auto_20191102_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ['-fecha_reserva', 'fecha_turno', 'hora_turno'], 'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
