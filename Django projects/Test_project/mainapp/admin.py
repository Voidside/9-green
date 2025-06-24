from django.contrib import admin

from .models import Category, Test

# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_on')



@admin.register(Test)
class Test_Admin(admin.ModelAdmin):
    list_display = ('question', 'category', 'true_answer')



