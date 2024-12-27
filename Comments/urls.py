from django.urls import path, include 
from rest_framework.routers import DefaultRouter 


from Comments.View.comments_api import  CommentViewSet 

routers = DefaultRouter()

routers.register(r'', CommentViewSet, basename='comments')




urlpatterns = [
    path('',include(routers.urls)),
]
