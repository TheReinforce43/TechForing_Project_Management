from rest_framework.viewsets import ViewSet

from User.models import Users 

from rest_framework.permissions import IsAuthenticated 
from User.Serializer.user_support_serializer import UserSerializer 
from User.models import Users 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.pagination import PageNumberPagination 



class UserAPIViewSet(ViewSet):
    permission_classes = [IsAuthenticated]


    # here using list api url 
    def list(self,request):
        paginator = PageNumberPagination()
        # define paginator size 
        paginator.page_size = 10

        # fetch query set 
        users  = Users.objects.all()

        result_page = paginator.paginate_queryset(users, request)

        # serialize the paginated queryset 
        serializer  =UserSerializer(result_page,many=True)

        return paginator.get_paginated_response(serializer.data)
    

    # api request for update request 

    def patch(self,request,pk=None):
        try:
            user = Users.objects.get(pk=pk)

        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

        serializer = UserSerializer(user,data=request.data )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

