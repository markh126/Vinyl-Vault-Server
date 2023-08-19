from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from vinylvaultapi.models import Record, User, Genre
from vinylvaultapi.serializers import RecordSerializer

class RecordView(ViewSet):
    """Vinyl Vault Record View"""
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
        serializer = RecordSerializer(records, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a new record"""
        user = User.objects.get(pk=request.data["userId"])
        genre = Genre.objects.get(pk=request.data["genreId"])
        record = Record.objects.create(
            name = request.data["name"],
            record_image_url = request.data["recordImageUrl"],
            artist = request.data["artist"],
            track_list = request.data["trackList"],
            genre = genre,
            release_date = request.data["releaseDate"],
            user = user
        )
        return Response({'message': 'Record Created'}, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a record"""
        record = Record.objects.get(pk=pk)
        genre = Genre.objects.get(pk=request.data["genreId"])
        user = User.objects.get(pk=request.data["userId"])
        record.name = request.data['name']
        record.record_image_url = request.data['recordImageUrl']
        record.artist = request.data['artist']
        record.track_list = request.data['trackList']
        record.genre = genre
        record.release_date = request.data['releaseDate']
        record.borrowed = request.data['borrowed']
        record.user = user
        record.save()
        return Response({'message': 'Record UPDATED'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to delete a record"""
        record = Record.objects.get(pk=pk)
        record.delete()
        return Response({'message': 'Record DELETED'}, status=status.HTTP_204_NO_CONTENT)