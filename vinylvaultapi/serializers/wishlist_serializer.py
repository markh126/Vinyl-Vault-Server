from rest_framework import serializers
from vinylvaultapi.models.wishlist_record import WishlistRecord
from vinylvaultapi.serializers import RecordSerializer, UserSerializer

class WishlistSerializer(RecordSerializer):
    """JSON serializer for wishlisted records"""
    record = RecordSerializer()
    user = UserSerializer()
    class Meta:
        model = WishlistRecord
        fields = ('id',
                  'record',
                  'user')