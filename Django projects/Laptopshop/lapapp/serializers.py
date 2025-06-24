from .models import Category, Sub_Category, Product, Branch
from rest_framework import serializers

class Product_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['sub_category', 'name', 'photo', 'description',\
                   'price', 'status',]

class Sub_Category_Serializer(serializers.HyperlinkedModelSerializer):
    products = Product_Serializer(many=True, read_only=True)

    class Meta:
        model = Sub_Category
        fields = ['id', 'category', 'name', 'photo', 'status', 'products']

class Category_Serializer(serializers.HyperlinkedModelSerializer):
    sub_categories = Sub_Category_Serializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', "status", 'sub_categories']





class Branch_Serializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'phone', 'work_time', \
                  'info', 'map_address', 'status']