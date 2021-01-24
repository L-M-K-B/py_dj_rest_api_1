from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list"""

        an_apiview = [
            'test1', 'test2', 'test3'
        ]
        return Response({'message': 'Hello! This is a test', 'an_apiview': an_apiview})

    def post(self, request):
        """creates a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating completely"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle updating partly"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    def list(self, request):
        """return a message saying hello"""

        a_viewset = [
            'test4', 'test5', 'test6'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})