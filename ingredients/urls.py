from django.urls import path
from .views import IngredientListCreateView, IngredientDetailView

urlpatterns = [
    path("", IngredientListCreateView.as_view()),
    path("<int:pk>/", IngredientDetailView.as_view()),
]
