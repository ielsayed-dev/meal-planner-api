
from rest_framework import serializers
from .models import Recipe, RecipeIngredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']