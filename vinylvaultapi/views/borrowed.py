from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from vinylvaultapi.models import BorrowedRecord, User
from vinylvaultapi.serializers import BorrowedSerializer

class BorrowedView(ViewSet):
    """Vinyl Vault Borrowed View"""
    def retrieve(self, request, pk):
        """GET request for a single borrowed record"""
        try:
            borrowed = BorrowedRecord.objects.get(pk=pk)
            serializer = BorrowedSerializer(borrowed)
            return Response(serializer.data)
        except BorrowedRecord.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of borrowed records"""
        borrowed_records = BorrowedRecord.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        borrowed_records = borrowed_records.filter(user=user)
        serializer = BorrowedSerializer(borrowed_records, many=True, context={'request': request})
        return Response(serializer.data)