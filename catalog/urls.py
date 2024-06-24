from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, IndexView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, ProductCreateView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products', ProductListView.as_view(), name='home'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='details'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete'),
    path('products/create', ProductCreateView.as_view(), name='create'),
    path('contacts', ContactsView.as_view(), name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
