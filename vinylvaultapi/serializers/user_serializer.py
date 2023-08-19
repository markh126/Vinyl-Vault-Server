from rest_framework import serializers
from vinylvaultapi.models.user import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'profile_image_url',
                  'email',
                  'username',
                  'bio',
                  'uid')
        depth = 1