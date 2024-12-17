from django.urls import path ,include

from User.View.user_creation_api import (
    UserSignUpView,
    UserLoginAPIView
)

from User.View.user_others_api import UserAPIViewSet

from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('users', UserAPIViewSet,basename='users')



urlpatterns = [
    path('signup/',UserSignUpView.as_view(),name='signup'),
    path('login/',UserLoginAPIView.as_view(),name='login'),
    path('',include(router.urls))
]
