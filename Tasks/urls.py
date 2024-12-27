from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 


# import related view set 

from Tasks.View.task_api import TaskViewSet

routers= DefaultRouter()

routers.register(r'',TaskViewSet)



urlpatterns = [
    path('',include(routers.urls)),
    
]

