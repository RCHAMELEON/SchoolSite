from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy,reverse
from news.forms import NewForm, UpdateForm
from django.shortcuts import render, redirect
from news.models import New


class NewCreate(CreateView):
    form_class = NewForm
    template_name = "news/create.html"

class NewUpdate(UpdateView):
    template_name = "news/update_new.html"
    model = New
    form_class = UpdateForm

    def get_object(self, queryset=None):
        new = New.objects.get(id=self.kwargs['new_id'])
        return new

class NewDelete(DeleteView):
    model = New
    template_name = "news/delete.html"
    success_url = reverse_lazy('index')
