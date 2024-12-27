from rest_framework.viewsets import ModelViewSet


# import related serializer and models 


from Tasks.Model.tasks_model import TaskModel 
from Tasks.Serializer.task_serializer import (
    CreateTaskSerializer,
    GetTaskSerializer
)

# create Task View set 

class TaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()
    
    def get_serializer_class(self):

        # this used for get all or retrieve by id data 
        if self.action in ['create','update']:
            return CreateTaskSerializer

        # this used for create ,update or delete the data 
        return GetTaskSerializer
