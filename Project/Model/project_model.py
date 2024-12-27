from django.db import models 
from django.utils.timezone import now 


from User.models import Users
 



class ProjectModel(models.Model):

    project_name = models.CharField(max_length=100)
    project_description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Users,related_name='project_owner',on_delete=models.CASCADE,null=True)
    project_start_date = models.DateTimeField(default=now)
    project_end_date = models.DateField(default=now)

    def __str__(self):
        return self.project_name
       # return f'{self.project_name} - {self.project_start_date}'