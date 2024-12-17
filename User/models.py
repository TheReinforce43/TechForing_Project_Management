from django.db import models 
from django.contrib.auth.models import AbstractUser

from User.custom_manager import UserManager
from django.utils.timezone import now 

#  I‘d: Primary Key
# Username: String (Unique)
# Email: String (Unique)
# Password: String
# First_name: String
# Last_name: String
# Date_joined: DateTime



class Users(AbstractUser):
    username= None 
    Username=models.CharField(max_length=100,unique=True)
    email= models.EmailField(max_length=150,unique=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    profile_image= models.ImageField(upload_to='images/',null=True,blank=True)
    date_joined=models.DateTimeField(default=now,null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Username']

    objects= UserManager()

