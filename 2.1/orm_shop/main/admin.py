from django.contrib import admin
from .models import Car, Client, Sale
from django.contrib import admin

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'color', 'mileage', 'volume', 'price')
    search_fields = ('model', 'color')
    list_filter = ('year',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'created_at')
    list_filter = ('created_at', 'car')