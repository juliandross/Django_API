# libreria de django urls
from django.urls import path, include
# Rest_framework
from rest_framework import routers
# Elementos de la app
from api import views

router=routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]