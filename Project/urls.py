from django.urls import path ,include 
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter 


# import related view 

from Project.View.project_api import  ProjectAPIViewSet
from Tasks.View.task_api import  TaskViewSet 

router = DefaultRouter()
router.register(r'projects', ProjectAPIViewSet,basename='projects')

# Nested router for tasks within a project

nested_task_router = NestedDefaultRouter(router,r'projects',lookup = 'project')
nested_task_router.register(r'tasks',TaskViewSet,basename='project-task')



urlpatterns = [
    path('',include(router.urls)),
    path('',include(nested_task_router.urls))
]





