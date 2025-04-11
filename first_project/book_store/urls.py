# book_store/urls.py
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.product, name='product_list'),  # This will show products on /books/
]
