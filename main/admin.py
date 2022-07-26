from django.contrib import admin
from .models import PopularCarModel


@admin.register(PopularCarModel)
class PopularCarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'is_active']
    list_display_links = ['brand', 'model']
    search_fields = ['brand', 'model', 'condition', 'motor_type']
    list_filter = ['created_at']

