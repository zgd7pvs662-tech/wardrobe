# clothes/urls.py
from django.urls import path, include # <-- Убедись, что 'include' импортирован
from . import views

app_name = 'clothes'

urlpatterns = [
    # --- URL-адреса страниц сайта ---
    path('', views.HomeView.as_view(), name='home'),
    path('wardrobe/', views.ItemListView.as_view(), name='item_list'),
    path('wardrobe/item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('wardrobe/add/', views.ItemCreateView.as_view(), name='item_create'),
    path('wardrobe/item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_update'),
    path('wardrobe/item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    
    path('outfits/', views.OutfitListView.as_view(), name='outfit_list'),
    path('outfits/add/', views.OutfitCreateView.as_view(), name='outfit_create'),
    path('outfits/<int:pk>/delete/', views.OutfitDeleteView.as_view(), name='outfit_delete'),
    path('outfits/<int:pk>/', views.OutfitDetailView.as_view(), name='outfit_detail'),
    path('outfits/<int:pk>/edit/', views.OutfitUpdateView.as_view(), name='outfit_update'),

    # --- НОВЫЙ КОД: ПОДКЛЮЧАЕМ URL-АДРЕСА API ---
    path('api/items/', include('clothes.api.urls')),
]