from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante-list'),
    path('estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante-create'),
    path('estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='estudiante-delete'),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('estudiantes/<int:estudiante_pk>/asignar-curso/', views.AsignarCursoView.as_view(), name='asignar-curso'),
    path('estudiantes/<int:estudiante_pk>/cursos/<int:curso_pk>/nota/nueva/', views.NotaCreateView.as_view(), name='nota-create'),
    path('notas/<int:pk>/editar/', views.NotaUpdateView.as_view(), name='nota-update'),
    path('notas/<int:pk>/eliminar/', views.NotaDeleteView.as_view(), name='nota-delete'),
    path('carreras/', views.CarreraListView.as_view(), name='carrera-list'),
    path('carreras/nueva/', views.CarreraCreateView.as_view(), name='carrera-create'),
    path('carreras/<int:pk>/editar/', views.CarreraUpdateView.as_view(), name='carrera-update'),
    path('carreras/<int:pk>/eliminar/', views.CarreraDeleteView.as_view(), name='carrera-delete'),
    path('carreras/<int:pk>/', views.CarreraDetailView.as_view(), name='carrera-detail'),
    path('carreras/<int:carrera_pk>/cursos/nuevo/', views.CursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='curso-delete'),
] 