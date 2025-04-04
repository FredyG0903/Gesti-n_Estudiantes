from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Estudiante, Curso
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

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
