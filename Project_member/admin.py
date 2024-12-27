from django.contrib import admin

# Register your models here.

from  Project_member.Model.project_member_model import ProjectUserModel

admin.site.register(ProjectUserModel)
