from rest_framework import serializers
from apps.departmants.models import (
    Department,
    Booking,
)
from apps.foods.serializers import FoodCategorySerializer


class DepartmentListSerializer(serializers.ModelSerializer):
    food = FoodCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'department', 'day', 'people',
            'number',
        )


class BookingListSerializer(serializers.ModelSerializer):
    department = DepartmentListSerializer()

    class Meta:
        model = Booking
        fields = "__all__"
