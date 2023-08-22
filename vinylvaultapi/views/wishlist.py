from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from vinylvaultapi.models import WishlistRecord, User
from vinylvaultapi.serializers import WishlistSerializer

class WishlistView(ViewSet):
    """Vinyl Vault Wishlist View"""
    def retrieve(self, request, pk):
        """GET request for a single wishlist"""
        try:
            wishlist = WishlistRecord.objects.get(pk=pk)
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        except WishlistRecord.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of wishlists"""
        wishlists = WishlistRecord.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        wishlists = wishlists.filter(user=user)
        serializer = WishlistSerializer(wishlists, many=True, context={'request': request})
        return Response(serializer.data)