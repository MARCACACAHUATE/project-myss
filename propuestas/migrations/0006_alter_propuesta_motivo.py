# Generated by Django 5.0.4 on 2024-05-17 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0005_alter_propuesta_motivo'),
        ('usuarios', '0004_asunto_motivo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='motivo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='usuarios.motivo'),
        ),
    ]
