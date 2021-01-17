from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test APIView"""

    def get(self, request, format=None):
        """returns a list"""

        an_apiview = [
            'test1', 'test2', 'test3'
        ]

        return Response({'message': 'Hello! This is a test', 'an_apiview': an_apiview})
