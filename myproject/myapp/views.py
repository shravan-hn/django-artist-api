from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['work_type']

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]
