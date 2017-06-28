from django import forms
from news.models import New
from ckeditor.widgets import CKEditorWidget

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'text', 'preview_picture', 'tags']
        #help_texts = {'tags': "Теги пишутся через запятую"}
        widgets = {"text": CKEditorWidget(),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'text', 'preview_picture', 'tags']
