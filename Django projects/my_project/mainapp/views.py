from django.shortcuts import render

from rest_framework import viewsets

from .models import Check_in
from .serializers import Checkin_Serializer

# Create your views here.

class Ceckin_Viewset(viewsets.ModelViewSet):
    queryset = Check_in.objects.all()
    serializer_class = Checkin_Serializer