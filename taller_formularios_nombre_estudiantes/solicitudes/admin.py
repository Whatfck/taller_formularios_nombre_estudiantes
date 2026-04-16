from django.contrib import admin
from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_solicitante',
        'tipo_solicitud',
        'correo_electronico',
        'fecha_solicitud'
    )
    list_filter = ('tipo_solicitud', 'fecha_solicitud')
    search_fields = ('nombre_solicitante', 'documento_identidad', 'correo_electronico')
    readonly_fields = ('fecha_solicitud',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_solicitante', 'documento_identidad', 'correo_electronico', 'telefono_contacto')
        }),
        ('Detalles de la Solicitud', {
            'fields': ('tipo_solicitud', 'asunto', 'descripcion_detallada')
        }),
        ('Archivo y Fecha', {
            'fields': ('archivo_adjunto', 'fecha_solicitud')
        }),
    )

