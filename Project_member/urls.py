from django.urls import path ,include 

from rest_framework.routers import DefaultRouter 

from Project_member.View.project_member_api import ProjectMemberViewSet

routers = DefaultRouter()

routers.register(r'',ProjectMemberViewSet)


urlpatterns = [
    path('',include(routers.urls))
]
