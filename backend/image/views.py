from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import UserSerializer, ImageSerializer
from .models import Image
from .helper import apply_filter   

User = get_user_model()

class ImageHandlingView(APIView):  
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            filtered_path = apply_filter(image_instance.image.path, image_instance.filter)

            return Response(
                {"message": "Image uploaded successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
