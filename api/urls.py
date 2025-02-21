from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
routers.register('Task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include('api.urls'))
]