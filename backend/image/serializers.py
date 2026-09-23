from rest_framework import serializers

from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "file_content", "sender", "filter", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at", "sender"] 