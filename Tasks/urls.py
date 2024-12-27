from django.urls import path ,include 
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter 


# import related view set 

from Tasks.View.task_api import TaskViewSet
from Comments.View.comments_api import CommentViewSet

router= DefaultRouter()

router.register(r'tasks',TaskViewSet,basename='tasks')


nested_comment_router = NestedDefaultRouter(router,r'tasks',lookup='task')
nested_comment_router.register(r'comments',CommentViewSet,basename='task-comments')


urlpatterns = [
    path('',include(router.urls)),
    path('',include(nested_comment_router.urls))
    
]

