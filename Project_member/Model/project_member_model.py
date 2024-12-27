from django.db import models 

# Import related models 
from User.models import Users 
from Project.Model.project_model import ProjectModel 

"""
I’d: Primary Key
Project: Foreign Key (to Projects)
User: Foreign Key (to Users)
Role: String (Admin, Member)
"""
from Supportive_snippets.code_snippets import role_snippets


class ProjectUserModel(models.Model):
    Project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE,related_name='projects')
    User = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='project_users')
    Role = models.CharField(max_length=10, choices=role_snippets)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'project :{self.project} , user:{self.user}'

