from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
#Clase tarea (modelo principal de la aplicación)
class Task(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    title = models.CharField(
        max_length=80,
        blank=False,
        null=False,
        validators=[MinLengthValidator(3, message="El título debe tener al menos 4 caracteres.")]
    )
    description = models.CharField(max_length=300,blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )