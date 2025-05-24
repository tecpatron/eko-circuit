from django.db import models
from django.contrib.auth.models import User

class Residuo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_residuos/', null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} ({self.estado})"

class RespuestaEncuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta1 = models.PositiveSmallIntegerField()
    pregunta2 = models.PositiveSmallIntegerField()
    pregunta3 = models.PositiveSmallIntegerField()
    pregunta4 = models.PositiveSmallIntegerField()
    pregunta5 = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuestas de {self.usuario.username}"

class ContadorVisitas(models.Model):
    visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitas: {self.visitas}"


