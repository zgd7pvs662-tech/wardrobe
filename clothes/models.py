# clothes/models.py
from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name="Название категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

class Item(models.Model):
    class Season(models.TextChoices):
        ANY = 'ANY', 'Любой сезон'
        SUMMER = 'SUM', 'Лето'
        WINTER = 'WIN', 'Зима'
        DEMI_SEASON = 'DEM', 'Демисезон'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Владелец"
    )
    name = models.CharField(max_length=200, verbose_name="Название вещи")
    category = models.ForeignKey( # <-- ВОЗВРАЩАЕМ КАТЕГОРИЮ
        Category,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to='clothes_images/%Y/%m/%d/',
        verbose_name="Изображение"
    )
    color = models.CharField(max_length=50, blank=True, verbose_name="Цвет")
    season = models.CharField(
        max_length=3,
        choices=Season.choices,
        default=Season.ANY,
        verbose_name="Сезон"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Вещь"
        verbose_name_plural = "Вещи"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clothes:item_detail', kwargs={'pk': self.pk})

class Outfit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='outfits',
        verbose_name="Владелец"
    )
    name = models.CharField(max_length=200, verbose_name="Название образа")
    items = models.ManyToManyField(
        Item,
        related_name='outfits',
        verbose_name="Вещи в образе"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Образ"
        verbose_name_plural = "Образы"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Мы еще не создали этот URL, но добавим его позже
        # return reverse('clothes:outfit_detail', kwargs={'pk': self.pk})
        pass