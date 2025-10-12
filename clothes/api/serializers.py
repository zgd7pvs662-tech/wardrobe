# clothes/api/serializers.py
from rest_framework import serializers
from clothes.models import Item # Импортируем модель Item из основного приложения clothes

class ItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Item.
    Преобразует данные модели в JSON.
    """
    class Meta:
        model = Item
        # Указываем поля, которые будут видны в API
        fields = ['id', 'name', 'user', 'color', 'season', 'image', 'created_at']