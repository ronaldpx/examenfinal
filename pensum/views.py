from django.shortcuts import render
from django.contrib import messages
from .forms import GradoForm
from pensum.models import Grado, Asignacion
# Create your views here.

def grado_nueva(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, grado_id = grado.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS,'Grado Guardada Exitosamente')

    else:
        formulario = GradoForm()
    return render(request, 'pensum/grado_editar.html', {'formulario': formulario})
