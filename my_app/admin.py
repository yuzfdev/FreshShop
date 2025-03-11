from django.contrib import admin
from .models import User_table,Products_table,Cart_table

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')
admin.site.register(User_table, UserAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('description', 'price')
admin.site.register(Products_table, ProductsAdmin)
