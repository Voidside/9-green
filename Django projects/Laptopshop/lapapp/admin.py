from django.contrib import admin

from .models import Category, Sub_Category, Product, Branch
# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)


@admin.register(Sub_Category)
class Sub_Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'status')
    list_filter = ('category', 'status')


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ('sub_category','name', 'description', 'price', 'status')
    search_fields = ('name', 'price', 'description')
    list_filter = ('sub_category','status')

@admin.register(Branch)
class Branch_Admin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'work_time')
    search_fields = ('name', 'info', 'address', 'phone')
    list_filter = ('status',)