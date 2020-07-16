from django.contrib import admin
from .models import Car, CarInstance, Brand

# Register your models here.

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(CarInstance)