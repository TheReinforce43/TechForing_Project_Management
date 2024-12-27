from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


# import related serializer and models 


from Tasks.Model.tasks_model import TaskModel 
from Project.Model.project_model import ProjectModel
from Tasks.Serializer.task_serializer import (
    CreateTaskSerializer,
    GetTaskSerializer
)

# create Task View set 

class TaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()


    def get_serializer_class(self):

        # this used for get all or retrieve by id data 
        if self.action in ['create','update','partial_update']:
            return CreateTaskSerializer

        # this used for create ,update or delete the data 
        return GetTaskSerializer
    

    def get_queryset(self):
        
        project_id = self.kwargs.get('project_pk')
        

        # project id exist then , retrieve related objects , otherwise return all 
        if project_id:
            return  TaskModel.objects.filter(Project_id=project_id)
        
        return  TaskModel.objects.all()
    
    
    def perform_create(self, serializer):
        
        # Ensure the project is included during task creation

        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(ProjectModel, id=project_id)


        
        serializer.save(Project=project)
        



