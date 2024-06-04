from django.core.exceptions import ValidationError
from django.forms import ModelForm, DecimalField, CharField, ModelChoiceField
from django.forms.widgets import Select

from catalog.models import Category, Product, Version


class ProductForm(ModelForm):
    name = CharField(label='Название товара')
    price = DecimalField(decimal_places=2)
    category = ModelChoiceField(queryset=Category.objects.all(),
                                widget=Select(attrs={'size': 4}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'image',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for bad_word in ['казино', 'криптовалюта', 'крипта', 'биржа',
                             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if bad_word in name.lower():
                raise ValidationError(f'{bad_word} - плохое слово')
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Отрицательная цена?')
        return price


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        labels = {'version': 'Наименование'}
