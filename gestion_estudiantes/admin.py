from django.contrib import admin
from .models import Carrera, Curso, Estudiante

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('duracion',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'carrera', 'semestre', 'creditos')
    search_fields = ('nombre', 'codigo')
    list_filter = ('carrera', 'semestre')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'carrera', 'sexo', 'situacion', 'fecha_registro')
    search_fields = ('nombre',)
    list_filter = ('carrera', 'situacion', 'sexo')
