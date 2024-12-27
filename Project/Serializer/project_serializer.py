from rest_framework import serializers 
from Project.Model.project_model import ProjectModel


# import serializer and models from User model 
from User.Serializer.user_support_serializer import UserSerializer
from User.models import Users



# create serializer for project model
class CreateProjectSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(),many=False)

    class Meta:
        model = ProjectModel
        fields ='__all__'



class Get_projectSerializers(serializers.ModelSerializer):

    owner=UserSerializer(read_only=True,many=False)

    class Meta:
        model = ProjectModel
        fields = '__all__'