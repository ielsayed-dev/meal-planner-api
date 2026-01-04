from django.urls import path
from .views import MealPlanListCreateView, MealPlanDetailView

urlpatterns = [
    path("", MealPlanListCreateView.as_view()),
    path("<int:pk>/", MealPlanDetailView.as_view()),
]
