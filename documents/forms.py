from documents.models import Document
from django import forms

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'desctiption', 'document_type', 'fiel', 'tags']
