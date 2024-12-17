from rest_framework import serializers 
from User.models import Users 

class UserSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Users
        exclude = ['password', 'groups','user_permissions','is_superuser','is_staff','last_login']

        