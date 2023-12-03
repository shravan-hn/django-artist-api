from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserSerializer  
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreate(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
