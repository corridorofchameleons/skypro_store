from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView, CreateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version


# APP_TITLE = 'SF Store'
# context = {'app_title': APP_TITLE}

# paginate_by = 3


class IndexView(TemplateView):
    template_name = 'catalog/index.html'


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_set'] = Version.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context.get('product')
        for v in product.versions.all():
            if v.current:
                context['version'] = v
                break
        if not context.get('version'):
            context['version'] = 'у продукта нет активной версии'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context.get('formset')
        if form.is_valid():

            # продукт до проверки не сохраняем
            product = form.save(commit=False)

            if formset.is_valid():
                formset.instance = product

                # версии сохраняем как есть
                formset.save()
                versions = Version.objects.filter(product=product)

                # счетчик текущих версий
                curr_cnt = 0

                for v in versions:
                    if v.current:
                        curr_cnt += 1

                # если больше одной текущей версии - привет, исключение!
                if curr_cnt > 1:
                    form.add_error(None, 'Только одна текущая категория допустима')
                    return self.render_to_response(self.get_context_data(form=form, formset=formset))

                # если все ок, сохраняем форму продукта
                else:
                    form.save()
                return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormSet(instance=self.object)
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


# def index(request):
#     return render(request, 'catalog/article_list.html')


# def product_list(request, page=1):
#
#     products = Product.objects.all()
#     pages = len(products) // paginate_by + 1
#
#     return render(request, 'catalog/product_list.html',
#                   context=context | {'products': products[paginate_by * (page - 1): paginate_by * page],
#                                      'pages': range(1, pages)})


# def product_details(request, pk):
#     product = Product.objects.filter(pk=pk).first()
#
#     print(product.image)
#     return render(request, 'catalog/product_detail.html',
#                   context=context | {'product': product})


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#         return redirect('catalog:home')
#
#     else:
#         contacts = Contact.objects.all().values()[0]
#         return render(request, 'catalog/contacts.html',
#                       context=context | contacts)
