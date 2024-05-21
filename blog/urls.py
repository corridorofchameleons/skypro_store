from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import index, ArticleListView, ArticleDetailView
from catalog.apps import CatalogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
