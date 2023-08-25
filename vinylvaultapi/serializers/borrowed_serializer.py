from rest_framework import serializers
from vinylvaultapi.models.borrowed_record import BorrowedRecord
from vinylvaultapi.serializers.record_serializer import RecordSerializer
from vinylvaultapi.serializers.user_serializer import UserSerializer

class BorrowedSerializer(RecordSerializer):
    """JSON serializer for borrowed records"""
    record = RecordSerializer()
    user = UserSerializer()
    class Meta:
        model = BorrowedRecord
        fields = ('id',
                  'record',
                  'user')