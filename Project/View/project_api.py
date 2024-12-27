
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response 
from rest_framework import status 


# import related model and serializer 
from Project.Model.project_model import ProjectModel 
from Project.Serializer.project_serializer import (
    CreateProjectSerializer,
    Get_projectSerializers
)




class ProjectAPIViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()

    def get_serializer_class(self):
        
        # this used for get all or retrieve by id data 
        if self.action in ['list','retrieve']:
            return Get_projectSerializers
        
        # this used for create ,update or delete the data 
        
        return CreateProjectSerializer
