from rest_framework import serializers
from vinylvaultapi.models.genre import Genre

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres"""
    class Meta:
        model = Genre
        fields = ('id',
                  'label')