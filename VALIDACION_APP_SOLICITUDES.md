# GUÍA DE VALIDACIÓN - APP SOLICITUDES (Persona B)

## ✅ Checklist antes de la Integración Final

### 1. Verificación de Archivos Creados
- [ ] solicitudes/models.py → Modelo Solicitud con 9 campos
- [ ] solicitudes/forms.py → ModelForm SolicitudForm
- [ ] solicitudes/views.py → 2 vistas (formulario, confirmacion)
- [ ] solicitudes/urls.py → Rutas configuradas
- [ ] solicitudes/admin.py → Admin personalizado
- [ ] solicitudes/templates/solicitudes/formulario.html → Plantilla del formulario
- [ ] solicitudes/templates/solicitudes/confirmacion.html → Plantilla de confirmación
- [ ] solicitudes/migrations/0001_initial.py → Migración creada

### 2. Verificación de Configuración
- [ ] settings.py: 'solicitudes' en INSTALLED_APPS
- [ ] settings.py: MEDIA_URL y MEDIA_ROOT configurados
- [ ] urls.py (proyecto): include("solicitudes.urls") agregado
- [ ] urls.py (proyecto): static(settings.MEDIA_URL) en DEBUG mode

### 3. Verificación de Base de Datos
- [ ] Tabla solicitudes_solicitud creada
- [ ] Campo id (Primary Key)
- [ ] Campo nombre_solicitante (CharField 150)
- [ ] Campo documento_identidad (CharField 50)
- [ ] Campo correo_electronico (EmailField)
- [ ] Campo telefono_contacto (CharField 20)
- [ ] Campo tipo_solicitud (CharField con choices)
- [ ] Campo asunto (CharField 255)
- [ ] Campo descripcion_detallada (TextField)
- [ ] Campo fecha_solicitud (DateField)
- [ ] Campo archivo_adjunto (FileField)

## 🧪 PRUEBAS FUNCIONALES

### Paso 1: Iniciar el Servidor
```bash
python manage.py runserver
```
Verificar que NO HAY ERRORES

### Paso 2: Acceder al Formulario
```
URL: http://localhost:8000/solicitudes/formulario/
```

**Validar:**
- [ ] Se carga la página sin errores
- [ ] Se ven todos los campos del formulario
- [ ] El diseño es claro y legible
- [ ] Formulario tiene CSS/estilos Bootstrap

### Paso 3: Prueba de Envío Exitoso
Completar el formulario con datos válidos:
- Nombre: "Juan Pérez"
- Documento: "1234567890"
- Email: "juan@example.com"
- Teléfono: "3001234567"
- Tipo: "Académica"
- Asunto: "Solicitud de calificación"
- Descripción: "Solicito revisión de la calificación..."
- Archivo: (opcional - puede dejar vacío o subir un archivo)

**Validar después de click "Enviar":**
- [ ] No hay errores de validación
- [ ] Se redirige a página de confirmación
- [ ] URL es: http://localhost:8000/solicitudes/confirmacion/1/
- [ ] Se muestra mensaje "¡Solicitud Enviada Exitosamente!"
- [ ] Se muestra referencia #1
- [ ] Se muestran todos los datos ingresados correctamente

### Paso 4: Verificar en Base de Datos (Admin)
```
URL: http://localhost:8000/admin/
Usuario: (crear con createsuperuser)
```

**Validar:**
- [ ] Sección "Solicitudes" visible
- [ ] El registro se ve en la lista
- [ ] Puedo hacer click y ver todos los detalles
- [ ] El filtro por "Tipo de solicitud" funciona
- [ ] La búsqueda funciona (por nombre o correo)

### Paso 5: Prueba de Validación
Intentar enviar con datos inválidos:
- [ ] Email vacío → mostrar error
- [ ] Email formato incorrecto → mostrar error
- [ ] Teléfono vacío → mostrar error
- [ ] Campo descripción vacío → mostrar error

### Paso 6: Prueba de Archivo
- [ ] Cargar un archivo (PDF/Imagen)
- [ ] Verificar que se guarda en media/solicitudes/
- [ ] En confirmación mostrar link para descargar

### Paso 7: Múltiples Solicitudes
Enviar 3 solicitudes diferentes
- [ ] Cada una obtiene un ID diferente
- [ ] Todas se guardan en la base de datos
- [ ] Se pueden ver todas en admin

## 📋 CAMPOS VERIFICAR UNO POR UNO

| Campo | Tipo | Requerido | Validación |
|-------|------|-----------|-----------|
| nombre_solicitante | Text(150) | ✓ | Max 150 caracteres |
| documento_identidad | Text | ✓ | Alfanumérico |
| correo_electronico | Email | ✓ | Formato email válido |
| telefono_contacto | Text(20) | ✓ | Números |
| tipo_solicitud | Select | ✓ | 4 opciones: académica, administrativa, técnica, otra |
| asunto | Text(255) | ✓ | Max 255 caracteres |
| descripcion_detallada | Textarea | ✓ | Sin límite de caracteres |
| fecha_solicitud | Date | Auto | Fecha actual automática |
| archivo_adjunto | File | ✗ | Opcional |

## 🔗 URLs CLAVE PARA PROBAR

| Descripción | URL |
|-------------|-----|
| Formulario | http://localhost:8000/solicitudes/formulario/ |
| Confirmación (ejemplo) | http://localhost:8000/solicitudes/confirmacion/1/ |
| Admin Solicitudes | http://localhost:8000/admin/solicitudes/solicitud/ |
| Admin principal | http://localhost:8000/admin/ |

## ❌ ERRORES COMUNES A EVITAR

- [ ] "No such table" → Ejecutar: python manage.py migrate
- [ ] "TemplateDoesNotExist" → Verificar ruta templates/solicitudes/
- [ ] "static files not found" → No es crítico en desarrollo
- [ ] Archivos no suben → Verificar MEDIA_ROOT en settings
- [ ] Form values se limpian → Validación fallida (ver mensajes de error)

## 💾 GUARDAR ANTES DE ENTREGAR

- [ ] Commit todos los cambios: `git add .` → `git commit -m "App Solicitudes completa"`
- [ ] Copiar URL para que Persona A pueda integrar
- [ ] Documento de este checklist completado
