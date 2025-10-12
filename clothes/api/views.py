# clothes/api/views.py
from rest_framework import generics
from clothes.models import Item # Импортируем модель Item
from .serializers import ItemSerializer # Импортируем сериализатор из этой же папки

# Этот View будет отдавать список всех вещей
class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Этот View будет отдавать одну вещь по ее id
class ItemDetailAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer