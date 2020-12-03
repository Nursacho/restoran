from django.contrib import admin
from apps.departmants.models import (
    Department,
    Booking,
)

admin.site.register(Department)
admin.site.register(Booking)
