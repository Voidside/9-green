from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class Product_Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'state', 'created_on')
    search_fields = ('name', 'state', 'created_on')
    list_filter = ('name', 'state', 'created_on')


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ('name', 'made_by', 'expiration_date', 'state', 'created_on')
    search_fields = ('name', 'made_by', 'serial_number')
    list_filter = ('category', 'made_by', 'expiration_date', 'state', 'created_on')