from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','text','domain','image', 'tags']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'domain', 'image', 'tags']
