
from rest_framework.viewsets import ModelViewSet

from Comments.Model.comments_model import CommentModel 

from Comments.Serializer.comments_serializer import (
    CreateCommentSerializer,
    Get_CommentSerializer
)


# this is comment model view set for CRUD Operations

class CommentViewSet(ModelViewSet):
    queryset = CommentModel.objects.all()

    def get_serializer_class(self):

        if self.action in ['create', 'update']:
            return CreateCommentSerializer

        return Get_CommentSerializer 