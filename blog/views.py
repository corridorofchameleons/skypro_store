from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from blog.models import Article


def index(request):
    return render(request, 'blog/article_list.html')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

