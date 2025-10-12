# clothes/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Этот путь (пустая строка) будет соответствовать /api/items/
    path('', views.ItemListAPIView.as_view(), name='api-item-list'),
    
    # Этот путь будет соответствовать /api/items/<id>/
    path('<int:pk>/', views.ItemDetailAPIView.as_view(), name='api-item-detail'),
]