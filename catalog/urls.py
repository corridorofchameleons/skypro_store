from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, product_details, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products', product_list, name='home'),
    path('products/page<int:page>', product_list, name='home'),
    path('products/<int:pk>', product_details, name='details'),
    path('contacts', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
