from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

MEAL_TYPES = [
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snack", "Snack"),
]

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)

    def __str__(self):
        return f"{self.meal_type} on {self.date}"
