from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from articles.forms import ArticleForm, UpdateForm
from django.shortcuts import render, redirect
from articles.models import Article


class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = "articles/create.html"

class ArticleUpdate(UpdateView):
    template_name = "articles/update_article.html"
    model = Article
    form_class = UpdateForm

    def get_object(self, queryset=None):
        article = Article.objects.get(id=self.kwargs['art_id'])
        return article

class ArticleDelete(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy('index')
