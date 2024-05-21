from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import index
from catalog.apps import CatalogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)