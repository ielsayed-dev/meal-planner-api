from rest_framework import serializers
from .models import MealPlan
from recipes.serializers import RecipeSerializer

class MealPlanSerializer(serializers.ModelSerializer):
    recipe_detail = RecipeSerializer(source="recipe", read_only=True)

    class Meta:
        model = MealPlan
        fields = "__all__"
        read_only_fields = ["user"]
