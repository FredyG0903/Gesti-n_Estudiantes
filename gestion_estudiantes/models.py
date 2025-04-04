from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    situacion = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo', verbose_name='Situación')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
