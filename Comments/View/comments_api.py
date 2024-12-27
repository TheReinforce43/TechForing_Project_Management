
from rest_framework.viewsets import ModelViewSet

# import related serializer and models
from Comments.Model.comments_model import CommentModel 
from Tasks.Model.tasks_model import TaskModel

from Comments.Serializer.comments_serializer import (
    CreateCommentSerializer,
    Get_CommentSerializer
)


from django.shortcuts import get_object_or_404

# this is comment model view set for CRUD Operations

class CommentViewSet(ModelViewSet):
    queryset = CommentModel.objects.all()

    def get_serializer_class(self):

        if self.action in ['create', 'update']:
            return CreateCommentSerializer

        return Get_CommentSerializer 
    
    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')

        # if task id exist ,the retrieve by task_id , otherwise all comments
        if task_id:
            return CommentModel.objects.filter(Task_id=task_id)
        
        return CommentModel.objects.all()
    

    # for automatically set the task id during comment creation

    def perform_create(self, serializer):
        task_id = self.kwargs.get('task_pk')
        task =get_object_or_404(TaskModel,id=task_id)

        serializer.save(Task=task)


        

