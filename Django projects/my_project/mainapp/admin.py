from django.contrib import admin

# Register your models here.

from .models import Check_in

@admin.register(Check_in)
class Chek_in_Admin(admin.ModelAdmin):
    list_display = ("full_name", "school")