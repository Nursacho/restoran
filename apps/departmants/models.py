from django.db import models
from apps.foods.models import FoodCategory


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
        null=True,
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
        return f"{self.title} -- {self.food}"
