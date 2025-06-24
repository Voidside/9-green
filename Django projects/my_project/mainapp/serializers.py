from rest_framework import serializers
from .models import Check_in

class Checkin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Check_in
        fields = "__all__"
