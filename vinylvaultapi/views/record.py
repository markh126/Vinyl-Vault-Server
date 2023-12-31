from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, filters
from vinylvaultapi.models import Record, User, Genre, WishlistRecord, BorrowedRecord
from vinylvaultapi.serializers import RecordSerializer

class RecordView(ViewSet):
    """Vinyl Vault Record View"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'artist']
    def retrieve(self, request, pk):
        """GET request for a single record"""
        try:
            record = Record.objects.get(pk=pk)
            serializer = RecordSerializer(record)
            return Response(serializer.data)
        except Record.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of records"""
        records = Record.objects.all()
        user = request.query_params.get('userId', None)
        uid = request.META['HTTP_AUTHORIZATION']
        record_user = User.objects.get(uid=uid)
        if user is not None:
            records = records.filter(user=user)
        for record in records:
            record.wishlisted = len(WishlistRecord.objects.filter(
                record=record, user=record_user
            )) > 0
        serializer = RecordSerializer(records, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a new record"""
        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        record = Record.objects.create(
            name = request.data["name"],
            record_image_url = request.data["recordImageUrl"],
            artist = request.data["artist"],
            spotify_id = request.data["spotifyId"],
            release_date = request.data["releaseDate"],
            user = user
        )
        serializer = RecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a record"""
        record = Record.objects.get(pk=pk)
        user = User.objects.get(pk=request.data["userId"])
        record.name = request.data['name']
        record.record_image_url = request.data['recordImageUrl']
        record.artist = request.data['artist']
        record.user = user
        record.save()
        return Response({'message': 'Record UPDATED'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to delete a record"""
        record = Record.objects.get(pk=pk)
        record.delete()
        return Response({'message': 'Record DELETED'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def add_to_wishlist(self, request, pk):
        """POST action to add a record to wishlist"""
        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        record = Record.objects.get(pk=pk)
        WishlistRecord.objects.create(
            user=user,
            record=record
        )
        return Response({'message': 'Added to Wishlist'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove_from_wishlist(self, request, pk):
        """DELETE action to remove a record from wishlist"""
        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        record = Record.objects.get(pk=pk)
        wishlist_record = WishlistRecord.objects.get(
            user = user,
            record = record
        )
        wishlist_record.delete()
        return Response({'message': 'Removed from Wishlist'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def borrow_record(self, request, pk):
        """POST action to borrow a record from another user"""
        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        record = Record.objects.get(pk=pk)
        BorrowedRecord.objects.create(
            user=user,
            record=record
        )
        return Response({'message': 'Record borrowed'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def return_record(self, request, pk):
        """DELETE action to return a borrowed record"""
        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        record = Record.objects.get(pk=pk)
        borrowed_record = BorrowedRecord.objects.get(
            user = user,
            record = record
        )
        borrowed_record.delete()
        return Response({'message': 'Record returned'}, status=status.HTTP_204_NO_CONTENT)
        