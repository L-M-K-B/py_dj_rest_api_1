from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serialises a name field for testing"""

    name= serializers.CharField(max_length=10)