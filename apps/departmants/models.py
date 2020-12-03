from django.db import models
from apps.foods.models import FoodCategory
from django.core.validators import RegexValidator

phone_number_regex = RegexValidator(
    regex=r'^(\+996)\d{9}$',
    message=(
        "Телефон должен быть в формате +996[код][номер]"
    )
)


class Department(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название место'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место расположения'
    )
    food = models.ManyToManyField(
        FoodCategory,
        related_name='department_food',
        blank=True,
        verbose_name='Кухня'
    )
    check = models.CharField(
        max_length=255,
        verbose_name='Средний счет'
    )
    seats = models.PositiveIntegerField(
        verbose_name='Количество мест',
        default=0
    )

    def __str__(self):
        return self.title


class Booking(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Место расположения',
        related_name='booking'
    )
    day = models.DateField(verbose_name='Дата')
    people = models.PositiveIntegerField(
        verbose_name='Число людей',
    )
    number = models.CharField(
        max_length=255,
        validators=[phone_number_regex],
        verbose_name='Телефон',
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.department.title} book's {self.day}"
