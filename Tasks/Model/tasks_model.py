from django.db import models 


# Import related models 
from Project.Model.project_model import ProjectModel 
from User.models import Users


from Supportive_snippets.code_snippets  import (
    status_snippets,
    priority_snippets
)

"""
I’d: Primary Key
Title: String
Description: Text
Status: String (To Do, In Progress, Done)
Priority: String (Low, Medium, High)
Assigned_to: Foreign Key (to Users, nullable)
Project: Foreign Key (to Projects)
Created_at: DateTime
Due_date: DateTime


"""


class TaskModel(models.Model):
    Title=models.CharField(max_length=200,unique=True)
    Description=models.TextField(null=True, blank=True)
    Status=models.CharField(max_length=20, choices=status_snippets,default='To Do')
    Priority=models.CharField(max_length=20, choices=priority_snippets,default='Low')
    Assigned_to=models.ForeignKey(Users, on_delete=models.CASCADE, related_name='assigned_user',null=True)
    Project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE, related_name='task_project',null=True)
    
    Created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Due_date=models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'task: {self.Title} '

