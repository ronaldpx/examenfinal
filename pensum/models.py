from django.db import models

from django.contrib import admin

class Materia(models.Model):
    nombre  =   models.CharField(max_length=100)
    creidto  =   models.IntegerField()
    profesor  =   models.CharField(max_length=100)



    def __str__(self):

        return self.nombre

class Grado(models.Model):
    nombre    = models.CharField(max_length=100)
    seccion      = models.CharField(max_length=25)
    materias  = models.ManyToManyField(Materia, through='Asignacion')


    def __str__(self):

        return self.nombre

class Asignacion (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)


class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class GradoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
