from django.shortcuts import render

from rest_framework import viewsets

from .models import Category, Test
from .serializers import Category_Serializer, Test_Serializer

# Create your views here.

class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer

class Test_Viewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = Test_Serializer