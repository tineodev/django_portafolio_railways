from django.db import models

# Create your models here.

class Project_model(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto_url = models.URLField(max_length=200)
    #!editar tags = models.CharField(max_length=100)
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return self.titulo + self.tags
