from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from blog.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


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
