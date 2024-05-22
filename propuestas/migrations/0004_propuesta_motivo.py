# Generated by Django 5.0.4 on 2024-05-17 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0003_alter_propuesta_status'),
        ('usuarios', '0004_asunto_motivo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='propuesta',
            name='motivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.motivo'),
        ),
    ]