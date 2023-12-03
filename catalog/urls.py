from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, product


app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]
