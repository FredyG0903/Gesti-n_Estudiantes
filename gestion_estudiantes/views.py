from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Estudiante, Curso
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    try:
        total_estudiantes = Estudiante.objects.count()
        estudiantes_activos = Estudiante.objects.filter(situacion='Activo').count()
        estudiantes_inactivos = Estudiante.objects.filter(situacion='Inactivo').count()
    except Exception as e:
        total_estudiantes = 0
        estudiantes_activos = 0
        estudiantes_inactivos = 0
        messages.error(request, f'Error al cargar las estadísticas: {str(e)}')

    context = {
        'total_estudiantes': total_estudiantes,
        'estudiantes_activos': estudiantes_activos,
        'estudiantes_inactivos': estudiantes_inactivos,
    }
    return render(request, 'gestion_estudiantes/inicio.html', context)

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_list.html'
    context_object_name = 'estudiantes'
    ordering = ['id']

class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_form.html'
    fields = ['nombre', 'fecha_nacimiento', 'sexo', 'situacion']
    success_url = reverse_lazy('estudiante-list')

    def form_valid(self, form):
        messages.success(self.request, 'Estudiante creado exitosamente.')
        return super().form_valid(form)

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_form.html'
    fields = ['nombre', 'fecha_nacimiento', 'sexo', 'situacion']
    success_url = reverse_lazy('estudiante-list')

    def form_valid(self, form):
        messages.success(self.request, 'Estudiante actualizado exitosamente.')
        return super().form_valid(form)

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Estudiante eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
