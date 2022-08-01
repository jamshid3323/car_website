from django.contrib import admin
from .models import PopularCarModel, FeaturedCarModel, MessageModel


@admin.register(PopularCarModel)
class PopularCarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'is_active']
    list_display_links = ['brand', 'model']
    search_fields = ['brand', 'model', 'condition', 'motor_type']
    list_filter = ['created_at']


@admin.register(FeaturedCarModel)
class FeaturedCarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'is_active']
    list_display_links = ['brand', 'model']
    search_fields = ['brand', 'model', 'price']
    list_filter = ['created_at']


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_display_links = ['name', 'email']
    list_filter = ['created_at']
