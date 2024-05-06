import json

from django.core.management import BaseCommand

from catalog.models import Category, Product

FILE = 'catalog/fixtures/data.json'


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(FILE) as f:
            data = json.load(f)

        result = []
        for d in data:
            if d.get('model') == 'catalog.category':
                result.append(d)

        return result

    @staticmethod
    def json_read_products():
        with open(FILE) as f:
            data = json.load(f)

        result = []
        for d in data:
            if d.get('model') == 'catalog.product':
                result.append(d)

        return result

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_to_create = []
        products_to_create = []

        for category in Command.json_read_categories():
            categories_to_create.append(
                Category(
                    id=category.get('pk'),
                    name=category.get('fields').get('name'),
                    description=category.get('fields').get('description'),
                )
            )

        Category.objects.bulk_create(categories_to_create)

        for product in Command.json_read_products():
            products_to_create.append(
                Product(
                    id=product.get('pk'),
                    name=product.get('fields').get('name'),
                    description=product.get('fields').get('description'),
                    image=product.get('fields').get('image'),
                    category=Category.objects.get(id=product.get('fields').get('category')),
                    price=product.get('fields').get('price'),
                    created_at=product.get('fields').get('created_at'),
                    updated_at=product.get('fields').get('updated_at'),
                )
            )

        Product.objects.bulk_create(products_to_create)
