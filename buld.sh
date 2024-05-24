#!/usr/bin/env bash

# Instalar dependencias de Python
pip install -r requirements.txt

# Instalar dependencias de Tailwind CSS
python manage.py tailwind install

# Compilar Tailwind CSS
python manage.py tailwind build

# Ejecutar migraciones
python manage.py migrate

# Recoger archivos estáticos
python manage.py collectstatic --no-input
