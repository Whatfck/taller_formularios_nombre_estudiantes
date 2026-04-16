from django.contrib import admin

from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_solicitante",
        "documento_identidad",
        "correo_electronico",
        "telefono_contacto",
        "tipo_solicitud",
        "fecha_solicitud",
    )
    list_filter = ("tipo_solicitud", "fecha_solicitud")
    search_fields = (
        "nombre_solicitante",
        "documento_identidad",
        "correo_electronico",
        "asunto",
    )
