# Generated by Django 5.0.4 on 2024-05-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_cerated_at_usuario_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
