
from rest_framework import serializers
from .models import food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ('__all__')