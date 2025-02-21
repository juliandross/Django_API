from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated 
from .permissions import isOwner
# ViewSet del modelo Task 
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    #Genera todos los cruds basicos y que utilice el serializador de Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    permission_classes = [IsAuthenticated, isOwner]

    def get_queryset(self):
        # Filtra las tareas para que cada usuario vea solo las suyas
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asigna automáticamente el propietario de la tarea al usuario autenticado
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)