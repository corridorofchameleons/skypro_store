from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
