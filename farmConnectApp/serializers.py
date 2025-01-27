from rest_framework import serializers


class NewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    Name = serializers.CharField()
    age = serializers.IntegerField()
    