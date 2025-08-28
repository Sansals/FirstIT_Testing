from django import forms
from .models import *

from django import forms
from django.utils import timezone
from .models import CashFlow


class CashFlowForm(forms.ModelForm):
    created_at = forms.DateField(
        required=False,  # делаем поле необязательным
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = CashFlow
        fields = ['created_at', 'status', 'tx_type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned = super().clean()

        # Если дата не указана, ставим текущую
        if not cleaned.get('created_at'):
            cleaned['created_at'] = timezone.now().date()

        return cleaned


""" CRUD-формы для статусов/типов/категорий/подкатегорий """
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TxTypeForm(forms.ModelForm):
    class Meta:
        model = TxType
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'tx_type']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']