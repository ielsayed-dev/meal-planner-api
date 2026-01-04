from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("categories/", include("categories.urls")),
    path("ingredients/", include("ingredients.urls")),
    path("recipes/", include("recipes.urls")),
    path("mealplans/", include("mealplans.urls")),
]
