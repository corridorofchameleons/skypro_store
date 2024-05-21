from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, \
    ArticleDeleteView
from catalog.apps import CatalogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('articles/<slug:slug>', ArticleDetailView.as_view(), name='details'),
    path('articles/<slug:slug>/update/', ArticleUpdateView.as_view(), name='update'),
    path('articles/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('articles/create/', ArticleCreateView.as_view(), name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
