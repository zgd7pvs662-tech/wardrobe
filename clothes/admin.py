# clothes/admin.py
from django.contrib import admin
from .models import Category, Item, Outfit # <-- ВОЗВРАЩАЕМ ИМПОРТ CATEGORY

@admin.register(Category) # <-- ВОЗВРАЩАЕМ АДМИНКУ ДЛЯ КАТЕГОРИЙ
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # <-- ВОЗВРАЩАЕМ CATEGORY В ОТОБРАЖЕНИЕ И ФИЛЬТРЫ
    list_display = ('name', 'category', 'user', 'season', 'created_at')
    list_filter = ('category', 'season', 'user')
    search_fields = ('name', 'color')
    date_hierarchy = 'created_at'
    list_select_related = ('category', 'user')

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('user',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    filter_horizontal = ('items',)