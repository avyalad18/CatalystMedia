from rest_framework import serializers
from apps.core.models import *


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20,allow_blank=False)
    password = serializers.CharField(max_length=20,allow_blank=False)


class AuthuserSerializer(serializers.ModelSerializer):
    class Meta :
        model = AuthUser
        fields = "__all__"