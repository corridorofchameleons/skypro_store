from django.conf import settings
from django.core.cache import cache
from catalog.models import Category


def get_category_list():
    key = 'category_list'
    if not settings.CACHE_ENABLED:
        return Category.objects.all()
    categories = cache.get(key)
    if not categories:
        categories = Category.objects.all()
        cache.set(key, categories)
        print('not in cache')
        return categories
    print('in cache')
    return categories
