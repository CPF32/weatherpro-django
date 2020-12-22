from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.city import City
from ..serializers import CitySerializer, UserSerializer

class Cities(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CitySerializer

    # Index Request
    def get(self, request):
        # filter only cities owned by user
        cities = City.objects.filter(owner=request.user.id)
        # serialize data
        data = CitySerializer(cities, many=True).data
        return Response({ 'cities': data })

    # Create Request
    def post(self, request):
        request.data['city']['owner'] = request.user.id
        city = CitySerializer(data=request.data['city'])
        if city.is_valid():
            city.save()
            return Response({ 'city': city.data }, status=status.HTTP_201_CREATED)
        return Response(city.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)

    # Delete Request
    def delete(self, request, pk):
        # get city for delete
        city = get_object_or_404(City, pk=pk)
        # confirm correct ownership rights
        if not request.user.id == city.owner.id:
            raise PermissionDenied('Unauthorized, you are not the owner of this city')

        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update Request
    def partial_update(self, request, pk):
        # remove owner or return false
        if request.data['city'].get('owner', False):
            del request.data['city']['owner']
        # locate city
        city = get_object_or_404(City, pk=pk)
        # confirm correct ownership rights
        if not request.user.id == city.owner.id:
            raise PermissionDenied('Unauthorized, you are not the owner of this city')

        request.data['city']['owner'] = request.user.id
        data = CitySerializer(city, data=request.data['city'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # error response if invalid data
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
