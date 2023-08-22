from rest_framework import serializers
from vinylvaultapi.models.borrowed_record import BorrowedRecord
from vinylvaultapi.serializers import RecordSerializer, UserSerializer

class BorrowedSerializer(RecordSerializer):
    """JSON serializer for genres"""
    record = RecordSerializer()
    user = UserSerializer()
    class Meta:
        model = BorrowedRecord
        fields = ('id',
                  'record',
                  'user')