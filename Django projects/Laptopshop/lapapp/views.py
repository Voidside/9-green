from django.shortcuts import render
from rest_framework import viewsets

from .models import Category, Sub_Category, Product, Branch

from .serializers import Category_Serializer, Sub_Category_Serializer, Product_Serializer, Branch_Serializer
# Create your views here.


class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer


class Sub_Category_ViewSet(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_Category_Serializer


class Product_ViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer


class Branch_ViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = Branch_Serializer