#!/usr/bin/env bash

# Instalar dependencias
pip install -r requirements.txt

python manage.py tailwind install

# Compilar Tailwind CSS
python manage.py tailwind build

# Ejecutar migraciones
python manage.py migrate

# Recoger archivos estáticos
python manage.py collectstatic --no-input