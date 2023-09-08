from rest_framework import serializers
from vinylvaultapi.models.record import Record
from vinylvaultapi.models.wishlist_record import WishlistRecord
from vinylvaultapi.models.borrowed_record import BorrowedRecord
from vinylvaultapi.serializers.user_serializer import UserSerializer

class RecordSerializer(serializers.ModelSerializer):
    """JSON serializer for records"""
    # Define a SerializerMethodField to include wishlisted data
    borrowed = serializers.SerializerMethodField()
    release_date = serializers.DateField(format="%m/%d/%Y")
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
                  'wishlisted',
                  'spotify_id',
                  'user')
        depth = 1
    
    def get_borrowed(self, obj):
        """Custom method to get borrowed status for the record"""
        return obj.borrowed
    
class WishlistSerializer(serializers.ModelSerializer):
    """JSON serializer for wishlisted records"""
    record = RecordSerializer()
    user = UserSerializer()
    class Meta:
        model = WishlistRecord
        fields = ('id',
                  'record',
                  'user')
        
class BorrowedSerializer(RecordSerializer):
    """JSON serializer for borrowed records"""
    record = RecordSerializer()
    user = UserSerializer()
    class Meta:
        model = BorrowedRecord
        fields = ('id',
                  'record',
                  'user')