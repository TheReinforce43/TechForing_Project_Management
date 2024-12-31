from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from User.models import Users
from User.Serializer.user_support_serializer import UserSerializer



class UserAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
   

    def partial_update(self, request, *args, **kwargs):
        """Handle PATCH requests to update a user."""
        try:
            user = self.get_object()  # Retrieve the user by primary key
        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
