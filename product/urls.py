from django.urls import path
from product import views


urlpatterns = [
    path('', views.view_products, name='product-list'),
    path('categories/', views.view_categories, name='category-list')
]