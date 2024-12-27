
from rest_framework import serializers 

from Tasks.Model.tasks_model import TaskModel 

from Project.Serializer.project_serializer import Get_projectSerializers 
from User.Serializer.user_support_serializer import UserSerializer



# Create Task Serializer 

class CreateTaskSerializer(serializers.ModelSerializer):


    class Meta:
        model = TaskModel
        fields='__all__'


# Get Task Serializer


class GetTaskSerializer(serializers.ModelSerializer):

    Project = Get_projectSerializers(read_only=True)
    Assigned_to = UserSerializer(read_only=True)


    class Meta:
        model = TaskModel
        fields='__all__'


    
