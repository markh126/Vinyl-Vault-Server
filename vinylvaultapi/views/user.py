from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from vinylvaultapi.models import User
from vinylvaultapi.serializers import UserSerializer

class UserView(ViewSet):
    """Feet First Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk):
        """PUT request to update a user"""
        user = User.objects.get(pk=pk)
        # uid = request.META['HTTP_AUTHORIZATION']
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.email = request.data['email']
        user.username = request.data['username']
        user.profile_image_url = request.data['profileImageUrl']
        user.bio = request.data['bio']
        # user.uid = uid
        user.save()
        return Response({'message': 'User UPDATED'}, status=status.HTTP_204_NO_CONTENT)