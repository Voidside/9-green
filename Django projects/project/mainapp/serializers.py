from .models import *
# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer



class Category_Serializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'photo', 'about']



class Product_Serializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'made_by', 'weight_mark', 'weight', 'photo',\
                   'serial_number', 'made_on', 'expiration_date', 'about']


# class Category_Serializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'



# class Product_Serializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'