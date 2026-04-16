from django.urls import path

from . import views

app_name = "asistencia"

urlpatterns = [
    path("", views.registrar_asistencia, name="formulario"),
    path("confirmacion/", views.confirmacion_asistencia, name="confirmacion"),
]
