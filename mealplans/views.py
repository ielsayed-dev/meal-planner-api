from rest_framework import generics, permissions
from .models import MealPlan
from .serializers import MealPlanSerializer

class MealPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)
