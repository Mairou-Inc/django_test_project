from django.contrib import admin
from shops.models import *

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Shop._meta.fields]
    raw_id_fields = ['city', 'street']

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Street._meta.fields]
    raw_id_fields = ['city']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=[field.name for field in City._meta.fields]

