from rest_framework import serializers 

# Import related serializers and models 
from User.Serializer.user_support_serializer import UserSerializer
from Project.Serializer.project_serializer import Get_projectSerializers 
from Project_member.Model.project_member_model import ProjectUserModel


# create project member serializer 

class CreateProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectUserModel
        fields='__all__'


# Get Project Member Serializer

class GetProjectMemberSerializer(serializers.ModelSerializer):

    User = UserSerializer(read_only=True)
    Project = Get_projectSerializers(read_only=True)


    class Meta:
        model = ProjectUserModel
        fields='__all__'