from django.contrib import admin
from articles.models import Article
# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
    model = Article
    fields = ['title', 'text', 'domain','image','tags']
    list_display = ['title','domain']
    search_fields = ['title','domain']

admin.site.register(Article, ArticlesAdmin)
