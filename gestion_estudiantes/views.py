from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Estudiante, Curso, Carrera
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

# Create your views here.

def inicio(request):
    try:
        total_estudiantes = Estudiante.objects.count()
        estudiantes_activos = Estudiante.objects.filter(situacion='Activo').count()
        estudiantes_inactivos = Estudiante.objects.filter(situacion='Inactivo').count()
        total_carreras = Carrera.objects.count()
        total_cursos = Curso.objects.count()
        carreras = Carrera.objects.all().order_by('nombre')[:5]  # Últimas 5 carreras
        cursos = Curso.objects.all().order_by('-id')[:5]  # Últimos 5 cursos
    except Exception as e:
        total_estudiantes = 0
        estudiantes_activos = 0
        estudiantes_inactivos = 0
        total_carreras = 0
        total_cursos = 0
        carreras = []
        cursos = []
        messages.error(request, f'Error al cargar las estadísticas: {str(e)}')

    context = {
        'total_estudiantes': total_estudiantes,
        'estudiantes_activos': estudiantes_activos,
        'estudiantes_inactivos': estudiantes_inactivos,
        'total_carreras': total_carreras,
        'total_cursos': total_cursos,
        'carreras': carreras,
        'cursos': cursos,
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

class CursoCreateView(CreateView):
    model = Curso
    template_name = 'gestion_estudiantes/curso_form.html'
    fields = ['nombre', 'codigo', 'creditos', 'semestre']
    
    def form_valid(self, form):
        form.instance.carrera = get_object_or_404(Carrera, pk=self.kwargs['carrera_pk'])
        messages.success(self.request, 'Curso creado exitosamente.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('carrera-detail', kwargs={'pk': self.kwargs['carrera_pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrera'] = get_object_or_404(Carrera, pk=self.kwargs['carrera_pk'])
        return context

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'gestion_estudiantes/curso_form.html'
    fields = ['nombre', 'codigo', 'creditos', 'semestre']
    
    def get_success_url(self):
        return reverse_lazy('carrera-detail', kwargs={'pk': self.object.carrera.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrera'] = self.object.carrera
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Curso actualizado exitosamente.')
        return super().form_valid(form)

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'gestion_estudiantes/curso_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('carrera-detail', kwargs={'pk': self.object.carrera.pk})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Curso eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'gestion_estudiantes/estudiante_detail.html'
    context_object_name = 'estudiante'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos_disponibles'] = Curso.objects.filter(carrera=self.object.carrera)
        return context

class AsignarCursoForm(forms.Form):
    curso = forms.ModelChoiceField(
        queryset=None, 
        label='Curso',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def __init__(self, carrera, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curso'].queryset = Curso.objects.filter(carrera=carrera)

class AsignarCursoView(FormView):
    template_name = 'gestion_estudiantes/asignar_curso.html'
    form_class = AsignarCursoForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.estudiante = get_object_or_404(Estudiante, pk=self.kwargs['estudiante_pk'])
        kwargs['carrera'] = self.estudiante.carrera
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiante'] = self.estudiante
        return context
    
    def form_valid(self, form):
        curso = form.cleaned_data['curso']
        estudiante = self.estudiante
        estudiante.cursos.add(curso)
        messages.success(self.request, f'Curso {curso.nombre} asignado exitosamente a {estudiante.nombre}.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('estudiante-detail', kwargs={'pk': self.estudiante.pk})
