from django.db import models

# import related models 

from Tasks.Model.tasks_model import TaskModel 
from User.models import Users


"""
I’d: Primary Key
Content: Text
User: Foreign Key (to Users)
Task: Foreign Key (to Tasks)
Created_at: DateTime

"""



class CommentModel(models.Model):

    Content = models.TextField()
    User = models.ForeignKey(Users,related_name='user_comments',on_delete=models.CASCADE)
    Task = models.ForeignKey(TaskModel,related_name='task_comments',on_delete=models.SET_NULL,null=True)

    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'user: {self.User.email}, content :{self.Content} '
    
