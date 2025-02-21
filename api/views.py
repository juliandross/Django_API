# rest_framework
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 
# modelos 
from django.contrib.auth.models import User
# elementos de la app
from .serializer import TaskSerializer, RegisterSerializer
from .models import Task
from .permissions import isOwner

#Para la documentación en swagger
from drf_yasg.utils import swagger_auto_schema
# ViewSet del modelo Task 
class TaskViewSet(viewsets.ModelViewSet):
    #Genera todos los cruds basicos y que utilice el serializador de Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #Tiene que ser el propietario y estar autenticado para hacer las solicitudes
    permission_classes = [IsAuthenticated, isOwner]
    #El get solo funciona para las tareas del usuario logeado
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # Asigna automáticamente el propietario de la tarea al usuario autenticado
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @swagger_auto_schema(
        operation_summary="Listar tareas",
        operation_description="Lista todas las tareas asociadas al usuario autenticado.",
        responses={200: TaskSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear tarea",
        operation_description="Crea una nueva tarea asignada automáticamente al usuario autenticado.",
        responses={201: TaskSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Obtener tarea",
        operation_description="Devuelve los detalles de una tarea específica usando su ID.",
        responses={200: TaskSerializer(), 404: 'No encontrado'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Eliminar tarea",
        operation_description="Elimina una tarea creada previamente por el usuario utilizando el ID para identificar la tarea",
        responses={200: TaskSerializer(), 404: 'No encontrado'},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Actualizar tarea",
        operation_description="Actualiza una tarea creada previamente por el usuario utilizando el ID para identificar la tarea",
        responses={200: TaskSerializer(), 404: 'No encontrado'},
    )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False) #Es un PUT así que la actualización no es parcial
        instance = self.get_object()  # Obtiene la tarea específica
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    

#Vista para las peticiones de registro de usuarios 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    #Permite el acceso sin autorización 
    #porque precisamente aún no existe la cuenta
    permission_classes = [AllowAny] 
    
    