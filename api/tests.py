#Libreria para pruebas 
from django.test import TestCase
# Modelos
from django.contrib.auth.models import User
# Para validaciones de error
from django.core.exceptions import ValidationError
# Sirve para traer una peticion por su nombre y no por su url
from django.urls import reverse
# Rest_framework
from rest_framework.test import APIClient
from rest_framework import status
# Elementos de la aplicación 
from .models import Task


#Pruebas para modelos
class TaskModelTest(TestCase):
    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.user = User.objects.create_user(username='user1', password='12345678')
        self.task = Task.objects.create(
            user=self.user,
            title="Tarea de prueba",
            description="Esto es solo una prueba",
            completed=False
        )
        
    # Verifica que la tarea se haya creado correctamente
    def test_task_creation(self):
        self.assertEqual(self.task.title, "Tarea de prueba")
        self.assertFalse(self.task.completed)
        
    # Verifica que la tarea esté asignada al usuario correcto
    def test_task_owner(self):
        self.assertEqual(self.task.user.username, "user1")
        
    # Verifica que la tarea pueda marcarse como completada
    def test_task_completion(self):
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)
        
    # Verifica que una tarea sin titulo no se puede publicar
    def test_task_without_title_should_fail(self):
        task = Task(user=self.user, description="Sin título")
        with self.assertRaises(ValidationError):
            task.full_clean() 
    
    # Verifica que una tarea que tenga menos de 3 caracteres no se pueda crear
    def test_task_title_min_length(self):
        short_title_task = Task(
            user=self.user, title="Hi", description="Título demasiado corto"
        )
        with self.assertRaises(ValidationError):
            short_title_task.full_clean()  
    
    # Verifica que se este asignando alguna fecha la tarea
    def test_task_creation_date(self):
        self.assertIsNotNone(self.task.created_at)
        
    
#Pruebas para endpoints
class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345678')
        self.client.login(username='testuser', password='12345678')

        # Crear una tarea de prueba
        self.task = Task.objects.create(
            user=self.user,
            title="Tarea de prueba",
            description="Esto es una tarea de prueba",
            completed=False
        )
        self.task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        self.list_url = reverse('task-list')  # Para el listado y creación de tareas
    
    # Verifica si funciona el endpoint para listar tareas
    def test_list_tasks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    # Verifica si funciona el endpoint para crear tarea 
    def test_create_task(self):
        data = {'title': 'Nueva tarea', 'description': 'Descripción nueva', 'completed': False}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Verifica si funciona el endpoint para obtener una tarea en especifico
    def test_retrieve_task(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Verifica si funciona el endpoint para actualizar una tarea en especifico
    def test_update_task(self):
        data = {'title': 'Tarea actualizada', 'description': 'Actualizada', 'completed': True}
        response = self.client.put(self.task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # Verifica si funciona el endpoint para eliminar una tarea en especifico
    def test_delete_task(self):
        response = self.client.delete(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

