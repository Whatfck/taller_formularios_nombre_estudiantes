from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('formulario/', views.solicitud_formulario, name='formulario'),
    path('confirmacion/<int:solicitud_id>/', views.solicitud_confirmacion, name='confirmacion'),
]
