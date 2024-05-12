# Generated by Django 5.0.4 on 2024-05-12 20:57

import propuestas.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0002_propuesta_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='status',
            field=models.CharField(default=propuestas.utils.Status['PENDIENTE'], max_length=30),
        ),
    ]
