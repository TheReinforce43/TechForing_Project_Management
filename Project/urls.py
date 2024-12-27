from django.urls import path ,include 
from rest_framework.routers import DefaultRouter

# import related view 

from Project.View.project_api import  ProjectAPIViewSet

router = DefaultRouter()
router.register(r'', ProjectAPIViewSet)



urlpatterns = [
    path('',include(router.urls))
]





