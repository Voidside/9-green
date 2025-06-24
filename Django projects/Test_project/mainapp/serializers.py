from rest_framework import serializers

from .models import Category, Test


class Test_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class Category_Serializer(serializers.ModelSerializer):

    tests = Test_Serializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'photo', 'description', 'tests']
