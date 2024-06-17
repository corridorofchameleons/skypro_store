from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView, CreateView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


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
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        product = Product.objects.select_related('user').get(pk=self.kwargs.get('pk'))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context.get('product')
        for v in product.versions.all():
            if v.current:
                context['version'] = v
                break
        if not context.get('version'):
            context['version'] = 'у продукта нет активной версии'

        # для сокращенного написания
        context['can_edit_moderator'] = self.request.user.groups.filter(name='moderator').exists()
        context['can_edit_author'] = self.request.user == self.object.user

        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        user = self.request.user
        product = form.save()
        product.user = user
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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

                # счетчик текущих версий
                curr_cnt = Version.objects.filter(product=product, current=True).count()

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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ProductForm
        if user.groups.filter(name='moderator').exists():
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        return self.request.user == self.get_object().user


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
