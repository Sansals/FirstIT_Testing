from django.contrib import admin
from .models import Status, TxType, Category, SubCategory, CashFlow


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(TxType)
class TxTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tx_type']
    list_filter = ['tx_type']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category__tx_type', 'category']
    search_fields = ['name']


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'status', 'tx_type', 'category', 'subcategory', 'amount']
    list_filter = ['created_at', 'status', 'tx_type', 'category', 'subcategory']
    search_fields = ['comment']
