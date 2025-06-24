from .models import *
from rest_framework import serializers

class Category_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class Product_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'