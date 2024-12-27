from rest_framework import serializers

# import related serializers 

from User.Serializer.user_support_serializer import UserSerializer
from Tasks.Serializer.task_serializer import GetTaskSerializer


# import related models
from Comments.Model.comments_model import CommentModel


# Create Comments  Serializer

class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = '__all__'



# Get Comments  Serializer

class Get_CommentSerializer(serializers.ModelSerializer):

    User=UserSerializer(read_only=True)
    Task=GetTaskSerializer(read_only=True)


    class Meta:
        model = CommentModel
        fields = '__all__'