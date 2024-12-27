
from rest_framework.viewsets import ModelViewSet 

# Import related serializer and models 

from Project_member.Model.project_member_model import ProjectUserModel
from Project_member.Serializer.project_member_serializer import (
    CreateProjectSerializer,
    GetProjectMemberSerializer
)


class ProjectMemberViewSet(ModelViewSet):

    queryset = ProjectUserModel.objects.all()


    def get_serializer_class(self):

        # this call when creating and updating a project
        if self.action in ['create','update']:
            return CreateProjectSerializer
        
        # this call when get all data, retrieving  or deleting a instance 
        return GetProjectMemberSerializer   