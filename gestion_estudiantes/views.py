from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Estudiante, Curso, Carrera
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    try:
        total_estudiantes = Estudiante.objects.count()
        estudiantes_activos = Estudiante.objects.filter(situacion='Activo').count()
        estudiantes_inactivos = Estudiante.objects.filter(situacion='Inactivo').count()
        total_carreras = Carrera.objects.count()
    except Exception as e:
        total_estudiantes = 0
        estudiantes_activos = 0
        estudiantes_inactivos = 0
        total_carreras = 0
        messages.error(request, f'Error al cargar las estadísticas: {str(e)}')

    context = {
        'total_estudiantes': total_estudiantes,
        'estudiantes_activos': estudiantes_activos,
        'estudiantes_inactivos': estudiantes_inactivos,
        'total_carreras': total_carreras,
    }
    return render(request, 'gestion_estudiantes/inicio.html', context)

class CarreraListView(ListView):
    model = Carrera
    template_name = 'gestion_estudiantes/carrera_list.html'
    context_object_name = 'carreras'
    ordering = ['nombre']

class CarreraCreateView(CreateView):
    model = Carrera
    template_name = 'gestion_estudiantes/carrera_form.html'
    fields = ['nombre', 'descripcion', 'duracion']
    success_url = reverse_lazy('carrera-list')

    def form_valid(self, form):
        messages.success(self.request, 'Carrera creada exitosamente.')
        return super().form_valid(form)

class CarreraUpdateView(UpdateView):
    model = Carrera
    template_name = 'gestion_estudiantes/carrera_form.html'
    fields = ['nombre', 'descripcion', 'duracion']
    success_url = reverse_lazy('carrera-list')

    def form_valid(self, form):
        messages.success(self.request, 'Carrera actualizada exitosamente.')
        return super().form_valid(form)

class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'gestion_estudiantes/carrera_confirm_delete.html'
    success_url = reverse_lazy('carrera-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Carrera eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

class CarreraDetailView(DetailView):
    model = Carrera
    template_name = 'gestion_estudiantes/carrera_detail.html'
    context_object_name = 'carrera'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = self.object.cursos.all().order_by('semestre', 'nombre')
        context['estudiantes'] = self.object.estudiantes.all()
        return context

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_list.html'
    context_object_name = 'estudiantes'
    ordering = ['nombre']

class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_form.html'
    fields = ['nombre', 'fecha_nacimiento', 'sexo', 'situacion', 'carrera']
    success_url = reverse_lazy('estudiante-list')

    def form_valid(self, form):
        messages.success(self.request, 'Estudiante creado exitosamente.')
        return super().form_valid(form)

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_form.html'
    fields = ['nombre', 'fecha_nacimiento', 'sexo', 'situacion', 'carrera']
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
