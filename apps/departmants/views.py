from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.foods.serializers import FoodListSerializer
from apps.departmants.models import Department
from apps.foods.models import Food
from apps.departmants.serializers import (
    DepartmentListSerializer,
    DepartmentSerializer
)


class DepartmentAPIViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=['get'])
    def foods(self, request, pk=None):
        departments = self.get_object()
        food = Food.objects.filter(category__in=departments.food.all())
        if food is not None:
            serializer = FoodListSerializer(food, many=True)
            return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DepartmentListSerializer
        return DepartmentSerializer
