# clothes/forms.py
from django import forms
from .models import Item, Outfit

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # Возвращаем 'category' в список полей
        fields = ['name', 'category', 'image', 'color', 'season']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Например, Белая футболка Uniqlo'}),
            'color': forms.TextInput(attrs={'placeholder': 'Белый, черный, синий'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'items', 'description']
        widgets = {
            'items': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Этот образ отлично подойдет для...'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['items'].queryset = Item.objects.filter(user=user)