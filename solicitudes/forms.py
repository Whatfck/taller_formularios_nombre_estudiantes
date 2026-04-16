from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono_contacto',
            'tipo_solicitud',
            'asunto',
            'descripcion_detallada',
            'archivo_adjunto'
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre completo'
                }
            ),
            'documento_identidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 1234567890'
                }
            ),
            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ejemplo@correo.com'
                }
            ),
            'telefono_contacto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 3001234567'
                }
            ),
            'tipo_solicitud': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Asunto de su solicitud'
                }
            ),
            'descripcion_detallada': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Describa en detalle su solicitud'
                }
            ),
            'archivo_adjunto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        labels = {
            'nombre_solicitante': 'Nombre del solicitante',
            'documento_identidad': 'Documento de identidad',
            'correo_electronico': 'Correo electrónico',
            'telefono_contacto': 'Teléfono de contacto',
            'tipo_solicitud': 'Tipo de solicitud',
            'asunto': 'Asunto',
            'descripcion_detallada': 'Descripción detallada',
            'archivo_adjunto': 'Archivo adjunto (opcional)',
        }
