# Generated by Django 2.2.6 on 2019-11-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20191101_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocancha',
            name='tipo_cancha',
            field=models.CharField(help_text='Ingrese el tipo de cancha.Ejemplo: Cancha 11, Cancha 7, etc.', max_length=50, unique=True, verbose_name='Tipo de cancha'),
        ),
    ]
