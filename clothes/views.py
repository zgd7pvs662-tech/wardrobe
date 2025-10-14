# clothes/views.py

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Item, Outfit
from .forms import ItemForm, OutfitForm

class HomeView(TemplateView):
    template_name = 'clothes/home.html'

# --- Views для Вещей (Item) ---

# ==============================================================================
# ↓↓↓ ЭТОТ БЛОК БЫЛ ИЗМЕНЕН ДЛЯ РАБОТЫ ФИЛЬТРОВ ↓↓↓
# ==============================================================================
class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'clothes/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        # Сначала получаем базовый набор данных: все вещи текущего пользователя
        queryset = super().get_queryset().filter(user=self.request.user)
        
        # Получаем значение фильтра 'season' из URL (например, ?season=summer)
        season_filter = self.request.GET.get('season')

        # Если фильтр был передан в URL и он не пустой/не 'all', применяем его
        if season_filter and season_filter != 'all':
            queryset = queryset.filter(season=season_filter)
        
        # Возвращаем отфильтрованный (или полный) список, сохранив оптимизацию
        return queryset.select_related('category')

    def get_context_data(self, **kwargs):
        # Сначала получаем базовый контекст от родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем в контекст имя текущего фильтра, чтобы подсветить кнопку в HTML
        # Если параметра 'season' нет, по умолчанию будет 'all'
        context['current_season'] = self.request.GET.get('season', 'all')
        
        return context
# ==============================================================================
# ↑↑↑ ИЗМЕНЕНИЯ ЗДЕСЬ ЗАКОНЧИЛИСЬ ↑↑↑
# ==============================================================================


class ItemDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Item
    template_name = 'clothes/item_detail.html'

    def test_func(self):
        item = self.get_object()
        return item.user == self.request.user

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'clothes/item_form.html'
    success_url = reverse_lazy('clothes:item_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'clothes/item_form.html'
    success_url = reverse_lazy('clothes:item_list')

    def test_func(self):
        item = self.get_object()
        return item.user == self.request.user

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'clothes/item_confirm_delete.html'
    success_url = reverse_lazy('clothes:item_list')

    def test_func(self):
        item = self.get_object()
        return item.user == self.request.user


# --- Views для Образов (Outfit) ---

class OutfitListView(LoginRequiredMixin, ListView):
    model = Outfit
    template_name = 'clothes/outfit_list.html'
    context_object_name = 'outfits'
    paginate_by = 9

    def get_queryset(self):
        return Outfit.objects.filter(user=self.request.user).prefetch_related('items')

class OutfitCreateView(LoginRequiredMixin, CreateView):
    model = Outfit
    form_class = OutfitForm
    template_name = 'clothes/outfit_form.html'
    success_url = reverse_lazy('clothes:outfit_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OutfitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Outfit
    template_name = 'clothes/outfit_confirm_delete.html'
    success_url = reverse_lazy('clothes:outfit_list')

    def test_func(self):
        outfit = self.get_object()
        return outfit.user == self.request.user

class OutfitDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Outfit
    template_name = 'clothes/outfit_detail.html'
    context_object_name = 'outfit'

    def test_func(self):
        outfit = self.get_object()
        return outfit.user == self.request.user

class OutfitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Outfit
    form_class = OutfitForm
    template_name = 'clothes/outfit_form.html' # Используем ту же форму, что и для создания
    success_url = reverse_lazy('clothes:outfit_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        outfit = self.get_object()
        return outfit.user == self.request.user