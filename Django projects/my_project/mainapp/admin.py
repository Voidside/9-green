from django.contrib import admin

# Register your models here.

from .models import Chek_in

@admin.register(Chek_in)
class Chek_in_Admin(admin.ModelAdmin):
    list_display = ("full_name", "school")