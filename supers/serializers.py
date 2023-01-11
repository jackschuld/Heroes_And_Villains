from rest_framework import serializers
from .models import Super

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'type']