from rest_framework import serializers
from vinylvaultapi.models.record import Record

class RecordSerializer(serializers.ModelSerializer):
    """JSON serializer for records"""
    class Meta:
        model = Record
        fields = ('id',
                  'name',
                  'record_image_url',
                  'artist',
                  'track_list',
                  'genre',
                  'release_date',
                  'borrowed',
                  'user')
        depth = 1