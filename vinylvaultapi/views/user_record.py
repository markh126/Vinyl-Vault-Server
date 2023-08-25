from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from vinylvaultapi.models import Record, WishlistRecord, BorrowedRecord, User
from vinylvaultapi.serializers import RecordSerializer
    
class UserRecordView(ViewSet):
    """Vinyl Vault Record View"""
    def list(self, request):
        """GET request for a list of records"""
        records = Record.objects.all()
        user = request.query_params.get('userId', None)
        if user is not None:
            records = records.filter(user=user)
        serializer = RecordSerializer(records, many=True, context={'request': request})
        return Response(serializer.data)