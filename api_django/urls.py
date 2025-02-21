#imports propios de urls y superusuario
from django.contrib import admin
from django.urls import path, include 
#imports de swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#Para validación JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
#Vistas para RegisterView
from api.views import RegisterView
#swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Django-API",
        default_version='v1',
        description="API en Django con autenticación por tokens o JWT. CRUD de tareas: GET/POST /tasks/, GET/PUT/DELETE /tasks/id/. Solo el creador puede modificar o eliminar.",
        terms_of_service="https://mit-license.org/",
        contact=openapi.Contact(email="julianalejandromunoz49@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),# Ruta para la interfaz gráfica del administrador de django
    path('api/', include('api.urls')),  # Todas las rutas de la app irán bajo /api/
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # Documentación de las URLS y modelos del proyecto
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # Documentación interactiva del proyecto
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Ruta para obtener un token 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Ruta para refrescar los tokens
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Ruta para verificar si un token es valido
    path('api/auth/', include('rest_framework.urls')),  # Autenticación por sesión
    path('api/register/', RegisterView.as_view(), name='register'),  # Registro bajo el prefijo api/
]

