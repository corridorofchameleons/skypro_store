from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.views += 1
        if item.views == 20:
            send_mail(
                'Congratulations!',
                f'The article {item.title} reached 20 views!',
                'constantgore@yandex.ru',
                ['constantgore@yandex.ru'],
                fail_silently=False,
            )
        item.save()
        return item


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')

    def form_valid(self, form):
        item = form.save()
        item.slug = slugify(item.title)
        item.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:details', kwargs=({'slug': self.object.slug}))


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')

    def get_success_url(self):
        return reverse('blog:details', kwargs=({'slug': self.object.slug}))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:index')
