from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *

# выносим метод в Mixin, чтобы исключить дублирование
class DictionariesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['transaction_types'] = TxType.objects.all()
        context['categories'] = Category.objects.select_related('tx_type')
        context['subcategories'] = SubCategory.objects.select_related(
            'category', 'category__tx_type'
        )
        return context

# главная
class CashFlowListView(DictionariesMixin, ListView):
    model = CashFlow
    template_name = 'cashflow/cashflow_list.html'
    paginate_by = 20

    #метод для фильтрации CashFlow
    def get_queryset(self):
        qs = super().get_queryset()

        # ключ = имя поля в фильтре, значение = параметр
        filters = {
            'created_at__gte': self.request.GET.get('date_from'),
            'created_at__lte': self.request.GET.get('date_to'),
            'status_id': self.request.GET.get('status'),
            'tx_type_id': self.request.GET.get('tx_type'),
            'category_id': self.request.GET.get('category'),
            'subcategory_id': self.request.GET.get('subcategory'),
        }

        # Применяем только те фильтры, которые не пустые
        filter_kwargs = {k: v for k, v in filters.items() if v}
        qs = qs.filter(**filter_kwargs)

        return qs

# CRUD для финансовых операций
class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form_generic.html'
    success_url = reverse_lazy('cashflow_list')
    extra_context = {
        "page_title": "Создать запись ДДС",
        "cancel_url": reverse_lazy("cashflow_list")
    }


class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form_generic.html'
    success_url = reverse_lazy('cashflow_list')
    extra_context = {
        "page_title": "Обновить запись ДДС",
        "cancel_url": reverse_lazy("cashflow_list")
    }


class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'cashflow/confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')
    extra_context = {
        'model_name': CashFlow._meta.verbose_name
    }

# Справочники
class DictListView(DictionariesMixin, TemplateView):
    template_name = 'cashflow/dict_list.html'


    """CRUD Справочников"""

# Статусы:

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Создать статус",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Обновить статус",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class StatusDeleteView(DeleteView):
    model = Status
    template_name = "cashflow/confirm_delete.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        'model_name': Status._meta.verbose_name
    }


# Типы

class TxTypeCreateView(CreateView):
    model = TxType
    form_class = TxTypeForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Создать тип транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class TxTypeUpdateView(UpdateView):
    model = TxType
    form_class = TxTypeForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Обновить тип транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class TxTypeDeleteView(DeleteView):
    model = TxType
    template_name = "cashflow/confirm_delete.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        'model_name': TxType._meta.verbose_name
    }


# Категории

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Создать категорию транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Обновить категорию транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "cashflow/confirm_delete.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        'model_name': Category._meta.verbose_name
    }


# Подкатегории

class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Создать подкатегорию транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "cashflow/form_generic.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        "page_title": "Обновить подкатегорию транзакции",
        "cancel_url": reverse_lazy("cashflow_list")
    }

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = "cashflow/confirm_delete.html"
    success_url = reverse_lazy("dict_list")
    extra_context = {
        'model_name': SubCategory._meta.verbose_name
    }