from django.db import models


class Solicitud(models.Model):
    TIPO_SOLICITUD_OPCIONES = [
        ("academica", "Academica"),
        ("administrativa", "Administrativa"),
        ("tecnica", "Tecnica"),
        ("otra", "Otra"),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    telefono_contacto = models.CharField(max_length=20)
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD_OPCIONES)
    asunto = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to="adjuntos_solicitudes/", blank=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
