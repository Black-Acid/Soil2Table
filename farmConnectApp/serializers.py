from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import UserModel, FarmDetailsModel



class FarmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmDetailsModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"]) # if frontend will be checking this then there will be no need for this
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
    