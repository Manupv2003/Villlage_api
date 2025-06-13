from rest_framework import serializers
from .models import LocalNews

class LocalNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalNews
        fields = '__all__'