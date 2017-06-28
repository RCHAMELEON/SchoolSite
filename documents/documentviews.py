from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from documents.forms import DocumentForm
from django.shortcuts import render, redirect
from documents.models import Document


class DocumentCreate(CreateView):
    form_class = DocumentForm
    template_name = "documents/create.html"


class DocumentDelete(DeleteView):
    model = Document
    template_name = "documents/delete.html"
    success_url = reverse_lazy('home')
