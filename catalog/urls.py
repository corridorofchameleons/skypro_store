from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts')
]
