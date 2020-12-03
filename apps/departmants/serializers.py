from rest_framework import serializers
from apps.departmants.models import (
    Department,
    Booking,
    PhoneNumber,
)
from apps.foods.serializers import FoodCategorySerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PhoneNumber
        fields = (
            'id', 'department',
            'number'
        )
        read_only_fields = ('department',)


class DepartmentListSerializer(serializers.ModelSerializer):
    food = FoodCategorySerializer(many=True, read_only=True)
    phone_number = PhoneNumberSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validated_data):
        phone_numbers = validated_data.pop('phone_number')
        instance = Department.objects.create(**validated_data)
        for phone_number in phone_numbers:
            PhoneNumber.objects.create(department=instance, **phone_number)
        return instance

    def update(self, instance, validated_data):
        phone_numbers = validated_data.pop('phone_number', [])
        for phone_number in phone_numbers:
            if phone_number.get('id') is None:
                phone_obj = PhoneNumber.objects.create(department=instance, **phone_number)
            else:
                phone_obj = PhoneNumber.objects.get(id=phone_number.get('id'))
                phone_obj.number = phone_number.get('number')
                phone_obj.save()
        return super().update(instance, validated_data)


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
