from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path("", RecipeListCreateView.as_view()),
    path("<int:pk>/", RecipeDetailView.as_view()),
]
