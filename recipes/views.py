from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)
