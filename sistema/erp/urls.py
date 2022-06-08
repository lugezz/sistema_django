from django.contrib import admin
from django.urls import path

from erp.views import *

app_name = 'erp'

urlpatterns = [
    #Categorias
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    #Productos
    path('product/list/', ProductListView.as_view(), name='product_list'),
    #Panel
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]