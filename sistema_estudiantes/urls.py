from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', include('gestion_estudiantes.urls')),
    path('', RedirectView.as_view(url='estudiantes/', permanent=True)),
] 