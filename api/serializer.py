# Modelos 
from django.contrib.auth.models import User
# Rest_framework serializadores
from rest_framework import serializers
# Elementos de la aplicación
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'user']
        read_only_fields = ['id', 'created_at', 'user']  # Evitar que el usuario pueda modificar estos campos

    def create(self, validated_data):
        # Asignar el usuario autenticado automáticamente
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    