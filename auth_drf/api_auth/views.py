from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import user_data
from .serializers import user_data_serializer

class user_data_viewset(viewsets.ModelViewSet):
    queryset = user_data.objects.all()
    serializer_class = user_data_serializer
    permission_classes =  [IsAuthenticated]