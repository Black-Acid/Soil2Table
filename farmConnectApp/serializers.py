from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import UserModel

class ConsumerSignUPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)
    
    class Meta:
        model = UserModel
        fields = ["email", "password", "confirm_password"]
    
    
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        
        if password != confirm_password:
            raise serializers.ValidationError("Passwords must Match")
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.get("password")
        validated_data["password"] = make_password(password)
        
        
        return UserModel.objects.create(**validated_data)
        











# class NewSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     Role = serializers.CharField()
#     Phone_number = serializers.IntegerField()
#     profile_picture = serializers.CharField()
#     password_hash = serializers.CharField()
#     updated_at = serializers.DateTimeField(read_only=True)
#     Address = serializers.CharField()
    