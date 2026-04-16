#!/usr/bin/env python
"""
Script para crear un superusuario de prueba automáticamente.
Úsalo una sola vez: python create_superuser.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_formularios_nombre_estudiantes.settings')
django.setup()

from django.contrib.auth.models import User

# Verificar si el superusuario ya existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✅ Superusuario creado exitosamente:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    print("   URL Admin: http://localhost:8000/admin/")
else:
    print("ℹ️ El superusuario 'admin' ya existe.")
    print("   Si necesitas cambiar la contraseña, usa:")
    print("   python manage.py changepassword admin")
