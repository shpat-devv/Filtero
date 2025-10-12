from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["pfp_url", "email"]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", None)
        user = User.objects.create_user(**validated_data)

        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)

        return user
