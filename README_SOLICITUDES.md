# 🚀 Taller 2 Django - App Solicitudes (Persona B)

## 📋 Estado del Proyecto

### ✅ Completado - App Solicitudes
- **Modelo Solicitud** con 9 campos según especificaciones
- **ModelForm** con validación automática
- **Vistas** para formulario y confirmación
- **Plantillas HTML** con diseño profesional (Bootstrap 5)
- **Admin personalizado** con filtros y búsqueda
- **URLs** configuradas y funcionales
- **Base de datos** migrada correctamente

---

## 🎯 Estructura de la App

```
solicitudes/
├── migrations/
│   ├── 0001_initial.py (Migración creada)
│   └── __init__.py
├── templates/solicitudes/
│   ├── formulario.html (Formulario del usuario)
│   └── confirmacion.html (Página de éxito)
├── admin.py (Solicitud registrada)
├── apps.py
├── forms.py (SolicitudForm)
├── models.py (Modelo Solicitud)
├── tests.py
├── urls.py (Rutas configuradas)
├── views.py (2 vistas)
└── __init__.py
```

---

## 🚀 INICIO RÁPIDO

### 1. Iniciar el servidor Django
```bash
python manage.py runserver
```

**Salida esperada:**
```
Starting development server at http://127.0.0.1:8000/
```

### 2. Acceder al formulario
Abre en el navegador:
```
http://localhost:8000/solicitudes/formulario/
```

### 3. Llenar el formulario
- Completa todos los campos requeridos
- El archivo es opcional
- Haz click en "Enviar Solicitud"

### 4. Confirmación
Se mostrará:
- ✅ Mensaje de éxito
- 📋 Resumen de datos
- 🆔 Número de referencia
- 🔗 Enlaces para nueva solicitud o admin

### 5. Verificar en Admin
```
http://localhost:8000/admin/
Usuario: admin
Contraseña: admin123
```

---

## 📊 Campos del Formulario

| Campo | Tipo | Validación | Ejemplo |
|-------|------|-----------|---------|
| **Nombre** | Texto | Max 150 chars | Juan Pérez García |
| **Documento** | Alfanumérico | - | 1234567890 |
| **Email** | Email | Formato válido | juan@example.com |
| **Teléfono** | Texto (20) | - | +573001234567 |
| **Tipo** | Select | 4 opciones | Académica |
| **Asunto** | Texto (255) | - | Revisión de calificación |
| **Descripción** | Textarea | - | Descripción detallada... |
| **Archivo** | File | Opcional | documento.pdf |
| **Fecha** | Auto | Automática | Hoy |

---

## 🔧 Configuración Importante

### En `settings.py`:
```python
INSTALLED_APPS = [
    ...
    "solicitudes",
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### En `urls.py` (proyecto):
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("solicitudes/", include("solicitudes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📱 URLs Disponibles

| Ruta | Descripción | Método |
|------|-------------|--------|
| `/solicitudes/formulario/` | Formulario de solicitud | GET/POST |
| `/solicitudes/confirmacion/<id>/` | Página de confirmación | GET |
| `/admin/` | Panel de administración | GET |

---

## 🧪 Casos de Prueba

### ✅ Prueba 1: Envío Exitoso
1. Accede a `/solicitudes/formulario/`
2. Completa todos los campos validamente
3. Click en "Enviar Solicitud"
4. **Resultado:** Redirección a confirmación con datos

### ✅ Prueba 2: Validación
1. Dejar campo email vacío
2. Click en "Enviar"
3. **Resultado:** Mostrar error "Este campo es obligatorio"

### ✅ Prueba 3: Email Inválido
1. Escribir "correoincorrecto" en email
2. Click en "Enviar"
3. **Resultado:** Mostrar error "Ingrese un correo válido"

### ✅ Prueba 4: Con Archivo
1. Llenar formulario completo
2. Seleccionar un archivo (PDF/Imagen)
3. Click en "Enviar"
4. **Resultado:** Archivo guardado en `media/solicitudes/`

### ✅ Prueba 5: Admin
1. Ir a `/admin/`
2. Iniciar sesión (admin/admin123)
3. Ver "Solicitudes"
4. **Resultado:** Ver todas las solicitudes guardadas
5. Filtrar por tipo de solicitud
6. Buscar por nombre

---

## 🐛 Si Hay Problemas

### Error: "No such table"
```bash
python manage.py migrate
```

### Error: "TemplateDoesNotExist"
Verificar que exista:
```
solicitudes/templates/solicitudes/formulario.html
solicitudes/templates/solicitudes/confirmacion.html
```

### Error: "ModuleNotFoundError"
```bash
python manage.py check
```

### No carga CSS/Bootstrap
Es normal en desarrollo, funciona correctamente en producción.

---

## 📝 Próximos Pasos (Integración)

### Esperando App de Persona A (Asistencia):
- [ ] Modelo Asistencia
- [ ] FormularioAsistencia
- [ ] Vistas de asistencia
- [ ] Templates de asistencia
- [ ] URLs de asistencia

### Integración Final (Ambos):
1. Registrar app asistencia en `INSTALLED_APPS`
2. Incluir URLs de asistencia en proyecto principal
3. Ejecutar migraciones finales
4. Pruebas conjuntas
5. Documentación

---

## 📚 Referencias

- [Django Forms Documentation](https://docs.djangoproject.com/en/6.0/topics/forms/)
- [Django Models](https://docs.djangoproject.com/en/6.0/topics/db/models/)
- [Django Admin](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/)

---

## 👤 Información de Trabajo

- **Persona B:** App Solicitudes (COMPLETADA ✅)
- **Persona A:** App Asistencia (En progreso)
- **Ambos:** Integración final y pruebas

---

## 📋 Checklist de Entrega

- [x] Modelo Solicitud creado y migrado
- [x] ModelForm funcional
- [x] Vistas GET/POST con validación
- [x] Redirección a confirmación correcta
- [x] Plantillas completas y claras
- [x] Registro en admin
- [x] URLs configuradas
- [x] Base de datos probada
- [x] Superusuario creado
- [x] Sistema check sin errores

---

**¡Listo para integración! 🎉**
