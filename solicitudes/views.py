from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Solicitud
from .forms import SolicitudForm


def solicitud_formulario(request):
    """
    Vista para mostrar el formulario de solicitud (GET)
    y procesar los datos enviados (POST)
    """
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save()
            return redirect('solicitudes:confirmacion', solicitud_id=solicitud.id)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = SolicitudForm()
    
    context = {
        'form': form,
    }
    return render(request, 'solicitudes/formulario.html', context)


def solicitud_confirmacion(request, solicitud_id):
    """
    Vista para mostrar el mensaje de confirmación
    y los datos de la solicitud registrada
    """
    solicitud = Solicitud.objects.get(id=solicitud_id)
    context = {
        'solicitud': solicitud,
    }
    return render(request, 'solicitudes/confirmacion.html', context)

