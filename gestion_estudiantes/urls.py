from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstudianteListView.as_view(), name='estudiante-list'),
    path('nuevo/', views.EstudianteCreateView.as_view(), name='estudiante-create'),
    path('editar/<int:pk>/', views.EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('eliminar/<int:pk>/', views.EstudianteDeleteView.as_view(), name='estudiante-delete'),
] 