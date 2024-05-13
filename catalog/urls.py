from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path('products', product_list, name='home'),
    path('products/<int:pk>', product_details, name='details'),
    path('contacts/', contacts, name='contacts')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
