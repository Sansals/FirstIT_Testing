from django.urls import path
from . import views

urlpatterns = [
    # CRUD для движений ДДС
    path('', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('<int:pk>/update/', views.CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),

    # для справочников
    path('dicts/', views.DictListView.as_view(), name='dict_list'),

    # Статусы
    path('dicts/status/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('dicts/status/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('dicts/status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),

    # Типы транзакций
    path('dicts/type/create/', views.TxTypeCreateView.as_view(), name='txtype_create'),
    path('dicts/type/<int:pk>/update/', views.TxTypeUpdateView.as_view(), name='txtype_update'),
    path('dicts/type/<int:pk>/delete/', views.TxTypeDeleteView.as_view(), name='txtype_delete'),

    # Категории
    path('dicts/category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('dicts/category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('dicts/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Подкатегории
    path('dicts/subcategory/create/', views.SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('dicts/subcategory/<int:pk>/update/', views.SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('dicts/subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='subcategory_delete'),
]
