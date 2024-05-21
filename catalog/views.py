from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView, CreateView

from catalog.models import Product, Contact

APP_TITLE = 'SF Store'
context = {'app_title': APP_TITLE}

paginate_by = 3


class IndexView(TemplateView):
    template_name = 'catalog/article_list.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')

    def form_valid(self, form):
        product = Product.objects.get(pk=self.object.pk)
        product.updated_at = timezone.now()
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.pk})


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
