from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstudianteListView.as_view(), name='estudiante-list'),
    path('nuevo/', views.EstudianteCreateView.as_view(), name='estudiante-create'),
    path('editar/<int:pk>/', views.EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('eliminar/<int:pk>/', views.EstudianteDeleteView.as_view(), name='estudiante-delete'),
    
    path('carreras/', views.CarreraListView.as_view(), name='carrera-list'),
    path('carreras/nueva/', views.CarreraCreateView.as_view(), name='carrera-create'),
    path('carreras/<int:pk>/', views.CarreraDetailView.as_view(), name='carrera-detail'),
    path('carreras/editar/<int:pk>/', views.CarreraUpdateView.as_view(), name='carrera-update'),
    path('carreras/eliminar/<int:pk>/', views.CarreraDeleteView.as_view(), name='carrera-delete'),
] 