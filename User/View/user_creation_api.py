from rest_framework.generics import (
    
    UpdateAPIView,
    CreateAPIView,
    
)

# import all related serializer and model 

from User.models import Users

from User.Serializer.user_serializer import (
    SignUpUserSerializer,
    LoggedInUserSerializer,
    UserLogoutSerializer
)
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 




# this create for user registration purposes

class UserSignUpView(CreateAPIView):
    serializer_class= SignUpUserSerializer
    queryset = Users.objects.all()



# this api view user login 

class UserLoginAPIView(APIView):
    serializer_class= LoggedInUserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data= request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user_data = serializer.validated_data 

            response_data ={
                "id": user_data["user"]['id'],
                "access_token": user_data["access_token"],
                "refresh_token": user_data["refresh_token"],
                "Username": user_data["user"]['Username'],
                "email": user_data["user"]["email"],
                "phone_number": user_data["user"]["phone_number"],
                "success": True
            }

            return Response(response_data,status= status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)



