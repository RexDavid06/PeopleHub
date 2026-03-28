from   rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    "inheriting form the serializer.Serializer class"
     
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=150)
        